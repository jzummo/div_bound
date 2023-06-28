import sympy as sp
import math

def maximize(p):
    a = (8 - math.log(p))/math.log(p)
    return (a + 1)/math.pow(p, a/8)

pl = list(sp.primerange(1, 2981))

C = 1
for p in pl:
    C *= maximize(p)

print(C)