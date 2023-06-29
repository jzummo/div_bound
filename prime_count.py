import sympy as sp
import random
import math

x = 0
while True:
    y = random.randint(0, pow(10, 10))
    if sp.isprime(y):
        break
    else:
        x += 1

print("The number of composite numbers reached before seeing a prime is", x)
print("Stirlings approximation for this number is", int(10 * math.log(10)))