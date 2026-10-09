#!/usr/bin/env python3
"""Validate skill metadata and package tracked skill files for a release."""

import argparse
import json
import re
import subprocess
import tomllib
from pathlib import Path, PurePosixPath
from urllib.parse import unquote, urlsplit
from zipfile import ZIP_DEFLATED, ZipFile

import yaml

EXCLUDED_DIRECTORIES = {
    "__pycache__",
    "venv",
    "env",
    "node_modules",
    "build",
    "dist",
}
EXCLUDED_SUFFIXES = {".pyc", ".pyo", ".olean", ".ilean"}
CLAUDE_METADATA = {
    PurePosixPath(".claude-plugin/plugin.json"),
    PurePosixPath(".claude-plugin/marketplace.json"),
}


def included(path):
    """Keep skill resources while excluding hidden and generated files."""
    return not (
        any(part.startswith(".") or part in EXCLUDED_DIRECTORIES for part in path.parts)
        or path.suffix in EXCLUDED_SUFFIXES
    )


def read_mapping(path):
    data = yaml.safe_load(path.read_text())
    if not isinstance(data, dict):
        raise TypeError(f"{path}: expected a YAML mapping")
    return data


def validate_skill(root, skill, files):
    path = root / skill / "SKILL.md"
    source = path.read_text()
    match = re.match(r"\A---\n(.*?)\n---(?:\n|\Z)", source, re.DOTALL)
    if not match:
        raise ValueError(f"{path}: missing YAML frontmatter")
    data = yaml.safe_load(match.group(1))
    if not isinstance(data, dict):
        raise TypeError(f"{path}: frontmatter must be a mapping")
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", skill) or len(skill) > 64:
        raise ValueError(f"{path}: invalid skill directory name")
    if data.get("name") != skill:
        raise ValueError(f"{path}: name must match the directory")
    description = data.get("description")
    if not isinstance(description, str) or not description.strip():
        raise ValueError(f"{path}: description must be a nonempty string")
    if len(description) > 1024 or "<" in description or ">" in description:
        raise ValueError(f"{path}: invalid description")
    if not source[match.end() :].strip():
        raise ValueError(f"{path}: instructions are empty")

    metadata = PurePosixPath(skill, "agents", "openai.yaml")
    if metadata not in files:
        raise ValueError(f"{metadata}: missing tracked UI metadata")
    interface = read_mapping(root / metadata).get("interface")
    if not isinstance(interface, dict):
        raise TypeError(f"{metadata}: missing interface mapping")
    for field in ("display_name", "short_description", "default_prompt"):
        value = interface.get(field)
        if not isinstance(value, str) or not value.strip():
            raise ValueError(f"{metadata}: {field} must be a nonempty string")
    if not 25 <= len(interface["short_description"]) <= 64:
        raise ValueError(f"{metadata}: short_description must be 25–64 characters")
    if f"${skill}" not in interface["default_prompt"]:
        raise ValueError(f"{metadata}: default_prompt must mention ${skill}")


def validate_links(root, files):
    for path in sorted(files):
        if path.suffix != ".md":
            continue
        for target in re.findall(r"\]\(([^)]+)\)", (root / path).read_text()):
            link = urlsplit(target.strip("<>"))
            if link.scheme or link.netloc or not link.path:
                continue
            resolved = (root / path.parent / unquote(link.path)).resolve()
            try:
                relative = PurePosixPath(resolved.relative_to(root).as_posix())
            except ValueError as exc:
                raise ValueError(f"{path}: link escapes repository: {target}") from exc
            if relative not in files:
                raise ValueError(f"{path}: link missing from package: {target}")


def validate_claude_metadata(root):
    """Check the root plugin/catalog contract and keep the release version aligned."""
    plugin = json.loads((root / ".claude-plugin/plugin.json").read_text())
    marketplace = json.loads((root / ".claude-plugin/marketplace.json").read_text())
    project = tomllib.loads((root / "pyproject.toml").read_text())["project"]
    if not isinstance(plugin, dict) or not isinstance(marketplace, dict):
        raise TypeError("Claude metadata must contain JSON objects")
    if plugin.get("name") != project["name"]:
        raise ValueError("Claude plugin name must match the project name")
    if plugin.get("version") != project["version"]:
        raise ValueError("Claude plugin version must match the project version")
    if plugin.get("skills") != ["./"]:
        raise ValueError("Claude plugin must scan the root skill directories")
    if (
        not isinstance(plugin.get("description"), str)
        or not plugin["description"].strip()
    ):
        raise ValueError("Claude plugin description must be a nonempty string")
    for label, owner in (
        ("plugin author", plugin.get("author")),
        ("marketplace owner", marketplace.get("owner")),
    ):
        if (
            not isinstance(owner, dict)
            or not isinstance(owner.get("name"), str)
            or not owner["name"].strip()
        ):
            raise ValueError(f"Claude {label} must have a nonempty name")
    if marketplace.get("name") != project["name"]:
        raise ValueError("Claude marketplace name must match the project name")
    entries = marketplace.get("plugins")
    if (
        not isinstance(entries, list)
        or len(entries) != 1
        or not isinstance(entries[0], dict)
    ):
        raise ValueError("Claude marketplace must contain the root plugin entry")
    entry = entries[0]
    if entry.get("name") != plugin["name"] or entry.get("source") != "./":
        raise ValueError("Claude marketplace entry must reference the root plugin")


def package(root, output):
    root = root.resolve()
    tracked = (
        subprocess.check_output(["git", "ls-files", "-z"], cwd=root)
        .decode()
        .split("\0")
    )
    skills = sorted(
        PurePosixPath(name).parts[0]
        for name in tracked
        if len(PurePosixPath(name).parts) == 2
        and PurePosixPath(name).name == "SKILL.md"
        and included(PurePosixPath(name))
    )
    if not skills:
        raise ValueError("No tracked skill directories found")
    files = {
        PurePosixPath(name)
        for name in tracked
        if name
        and PurePosixPath(name).parts[0] in skills
        and included(PurePosixPath(name))
    }
    if not CLAUDE_METADATA <= {PurePosixPath(name) for name in tracked if name}:
        raise ValueError("Claude plugin and marketplace metadata must be tracked")
    files.update(CLAUDE_METADATA)
    for path in files:
        if (root / path).is_symlink() or not (root / path).is_file():
            raise ValueError(f"{path}: expected a regular tracked file")
    for skill in skills:
        validate_skill(root, skill, files)
    validate_claude_metadata(root)
    validate_links(root, files)

    output.parent.mkdir(parents=True, exist_ok=True)
    with ZipFile(output, "w", compression=ZIP_DEFLATED) as archive:
        for path in sorted(files):
            archive.write(root / path, arcname=str(path))
    print(f"Validated {len(skills)} skills; packaged {len(files)} files in {output}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    try:
        package(root, args.output.resolve())
    except (
        TypeError,
        ValueError,
        OSError,
        yaml.YAMLError,
        subprocess.CalledProcessError,
    ) as exc:
        parser.exit(1, f"Skill release validation failed: {exc}\n")


if __name__ == "__main__":
    main()
