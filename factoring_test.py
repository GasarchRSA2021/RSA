"""
Program to test out factoring_test.py
"""

# Imports factoring.py to use the file's functions etc -> can call module by mRSA instead of RSAEncryption
import factoring as f

# Asks for N and B
N = int(input("Enter N to be factored: "))
#B = int(input("Enter smoothness bound B: "))

# Prints factor by quad sieve
#print("\nFactor: ", f.quadSieve(N, B))

#print("\nFactor: ", f.pollardrho(N, f="x**2+1"))
print("\nFactor: ", f.fermat(N))

p, q = f.trivial(N)
print("\nFactors: ", p, ", ", q)