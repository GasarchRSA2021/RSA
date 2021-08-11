import helper
import rsa_encryption as rsa
import factoring as factor
import time
import sympy


def countTime(func, t):
    start = time.time()
    p, q = func(t)
    print (p, q)
    end = time.time()
    return end - start

def readFile(file="pq.txt"):
    f = open(file, "r")
    for line in f:
        p, q = line.split()
        n = int(p)*int(q)
        print(p, q, n)
        print("pollard rho:", countTime(factor.pollardrho, n))
        #print("Quad Sieve:", countTime(factor.quadSieve, n))
        #print("Trivial", countTime(factor.trivial, n))
        #print("Trivial2", countTime(factor.trivial2, n))
        #print("Fermat", countTime(factor.fermat, n))


readFile()

# print("pollard rho:", countTime(f.pollardrho, 56421059))
# print("Quad Sieve:", countTime(f.quadSieve, n))
# print("Trivial", countTime(f.trivial, n))
# print("Trivial2", countTime(f.trivial2, n))
# print("Fermat", countTime(f.fermat, n))
