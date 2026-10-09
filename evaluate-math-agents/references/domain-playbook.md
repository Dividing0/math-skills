# Controlled task-level evaluation

## Choose a branch
- Capability audit: define correctness and hypothesis handling for each task before observing responses. Use exact witnesses, independently checked calculations or a private mathematical rubric; a fluent explanation is not a correctness oracle.
- Skill comparison: hold model, tools, token budget and task inputs fixed, randomize condition order, and use fresh paired tasks. Record failure modes as well as aggregate scores. The tested population is the task distribution actually sampled.
- Regression gate: freeze previously discovered failures and add new hidden tasks. A pass on a public acceptance example verifies a requirement but cannot measure generalization to hidden problems.

## Worked calculation
Suppose six independent task pairs are graded correct or incorrect. Skill condition outcomes are [1,1,1,0,1,0]; control outcomes are [1,0,1,1,0,0]. The skill scores 4/6 and control 3/6; paired differences are [0,1,0,-1,1,0], so the mean difference is 1/6. There are two skill-only successes and one control-only success. This is a small descriptive result with three discordant pairs, not a reliable general improvement estimate. Report all six outcomes and assess why the failed pair changed.

## Tempting inference and counterexample
An evaluator can inflate performance by treating generated tasks as independent despite duplicated reasoning. One hundred copies of a single solved contraction example give 100/100 correctness while saying nothing about a compact noncontraction or an incomplete domain. The nominal sample count is 100 but the task variety is one. Group related templates and report results by failure class, including uncertainty from the actual independent unit.

## Stop or hand off
If expected answers were visible to solvers, mark the test contaminated and replace those tasks before making a held-out claim. If budgets differ, report an uncontrolled comparison rather than attributing a difference to the skill. Hand ambiguous mathematical scoring to an independent reviewer with anonymized outputs and the exact rubric. Save prompts, response transcripts, version hashes, tool runs, scoring decisions and disagreement resolutions. Do not label manual document inspection as an executed downstream agent test.
