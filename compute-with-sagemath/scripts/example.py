
if not __debug__:
    raise RuntimeError('Verification requires Python assertions enabled; do not use -O or PYTHONOPTIMIZE.')

import argparse, json, sys
parser=argparse.ArgumentParser()
parser.add_argument("--self-test",action="store_true",help="Run independent oracle checks (also run by default)")
args=parser.parse_args()
try:
    from sage.all import PolynomialRing,QQ,GF
    from sage.env import SAGE_VERSION
    def compute():
        R=PolynomialRing(QQ,"x")
        x=R.gen()
        p=x**2+1
        fac_q=p.factor()
        assert fac_q.prod()==p
        assert p.is_irreducible()
        T=PolynomialRing(GF(5),"x")
        y=T.gen()
        q=y**2+1
        fac_f=q.factor()
        assert fac_f.prod()==q
        roots=q.roots()
        residues=[k for k in range(5) if (k*k+1)%5==0]
        assert sorted(int(r) for r,m in roots)==residues==[2,3]
        assert all(m==1 for r,m in roots)
        return {"QQ_factorization":str(fac_q),"GF5_factorization":str(fac_f),"parents":[str(p.parent()),str(q.parent())],"roots_mod5":residues,"validation":"exact-algebra-reconstructed","version":SAGE_VERSION}
    result=compute()
    result["self_test"]="passed"
    print(json.dumps(result,ensure_ascii=False,sort_keys=True))
except ModuleNotFoundError as exc:
    print(json.dumps({'status':'dependency-unavailable','dependency':exc.name}))
    sys.exit(2)
except Exception as exc:
    print(json.dumps({"status":"failed","error_type":type(exc).__name__,"error":str(exc)}),file=sys.stderr)
    sys.exit(1)
