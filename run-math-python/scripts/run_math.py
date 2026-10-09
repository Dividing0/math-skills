"""Run an authorized Python script and persist source, logs and environment evidence.
This is a process runner, not a security sandbox or a mathematical proof checker.
"""

if not __debug__:
    raise RuntimeError('Verification requires Python assertions enabled; do not use -O or PYTHONOPTIMIZE.')

import argparse,hashlib,json,os,platform,signal,subprocess,sys,tempfile,time
from pathlib import Path

def run(script,out,python,timeout,packages=(),seed=0,arguments=()):
    script=Path(script).resolve();out=Path(out).resolve()
    if not script.is_file():raise ValueError('script must be a regular file')
    if timeout<=0:raise ValueError('timeout must be positive')
    if out.exists():raise ValueError('output directory already exists; choose a new path')
    out.mkdir(parents=True)
    source=script.read_bytes();(out/'source.py').write_bytes(source)
    probe='import sys,json,importlib.metadata as m; r={};\nfor p in sys.argv[1:]:\n try:r[p]=m.version(p)\n except m.PackageNotFoundError:r[p]=None\nprint(json.dumps({"python":sys.version,"packages":r}))'
    env=os.environ.copy();env['MATH_EXPERIMENT_SEED']=str(seed)
    env.setdefault('MPLBACKEND','Agg')
    try:
        metadata=subprocess.run([python,'-c',probe,*packages],capture_output=True,text=True,timeout=10,check=True)
        versions=json.loads(metadata.stdout)
    except (OSError,subprocess.SubprocessError,ValueError) as error:
        versions={'probe_error':str(error)}
    command=[python,str(script),*arguments];start=time.monotonic();timed_out=False
    with (out/'stdout.txt').open('wb') as stdout,(out/'stderr.txt').open('wb') as stderr:
        try:
            process=subprocess.Popen(command,cwd=out,env=env,stdout=stdout,stderr=stderr,start_new_session=(os.name=='posix'))
            try:returncode=process.wait(timeout=timeout)
            except subprocess.TimeoutExpired:
                timed_out=True
                if os.name=='posix':os.killpg(process.pid,signal.SIGKILL)
                else:process.kill()
                returncode=process.wait()
        except OSError as error:
            stderr.write(str(error).encode());returncode=127
    result={'command':command,'working_directory':str(out),'source_sha256':hashlib.sha256(source).hexdigest(),
            'environment':versions,'platform':platform.platform(),'seed_environment_value':seed,
            'seed_scope':'script must explicitly seed its RNG; environment value alone does not do so',
            'timeout_seconds':timeout,'elapsed_seconds':time.monotonic()-start,'returncode':returncode,
            'status':'timeout' if timed_out else ('completed' if returncode==0 else 'failed'),
            'evidence_scope':'execution outcome only; mathematical validity must be checked separately',
            'artifacts':['source.py','stdout.txt','stderr.txt','run.json']}
    (out/'run.json').write_text(json.dumps(result,indent=2));return result

def self_test(python):
    with tempfile.TemporaryDirectory() as tmp:
        root=Path(tmp);script=root/'job.py'
        script.write_text('import json,os; print(json.dumps({"value":6*7,"seed":os.environ["MATH_EXPERIMENT_SEED"]}))')
        good=run(script,root/'good',python,5,['numpy'],13)
        assert good['status']=='completed'
        assert json.loads((root/'good/stdout.txt').read_text())=={'value':42,'seed':'13'}
        assert (root/'good/source.py').read_bytes()==script.read_bytes()
        script.write_text('import sys; print("intentional failure",file=sys.stderr); sys.exit(7)')
        bad=run(script,root/'bad',python,5);assert bad['status']=='failed' and bad['returncode']==7
        assert 'intentional failure' in (root/'bad/stderr.txt').read_text()
        script.write_text('import time; time.sleep(10)')
        slow=run(script,root/'slow',python,0.2);assert slow['status']=='timeout'
        for args in [(script,root/'good',python,1),(script,root/'negative',python,0)]:
            try:run(*args)
            except ValueError:pass
            else:raise AssertionError('bad request accepted')
        return {'checks':['success_and_seed','source_snapshot','failure_and_stderr','timeout','existing_output_rejected','nonpositive_timeout_rejected'],'status':'pass'}

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--script');parser.add_argument('--out');parser.add_argument('--python',default=sys.executable)
    parser.add_argument('--timeout',type=float,default=60);parser.add_argument('--seed',type=int,default=0)
    parser.add_argument('--package',action='append',default=[]);parser.add_argument('--self-test',action='store_true')
    parser.add_argument('arguments',nargs=argparse.REMAINDER)
    args=parser.parse_args()
    if args.self_test:print(json.dumps(self_test(args.python)));sys.exit(0)
    if not args.script or not args.out:parser.error('--script and --out are required')
    try:
        remaining=args.arguments[1:] if args.arguments[:1]==['--'] else args.arguments
        result=run(args.script,args.out,args.python,args.timeout,args.package,args.seed,remaining)
        print(json.dumps(result,indent=2))
        sys.exit(124 if result['status']=='timeout' else (0 if result['returncode']==0 else 1))
    except ValueError as error:parser.error(str(error))
