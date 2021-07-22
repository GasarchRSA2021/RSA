"""
Program for encryption and decryption given p, q, and e
"""
import sympy
import math

# Creates a class for encrypting and decrypting given p, q, e, and m
# Stores inside of object
class RSA:
    
    def generatePrimes(L):
        p = sympy.randprime(2, L)
        q = sympy.randprime(2, L)
        print(p, q)
        return p, q

    def is_coprime(e, p, q):
        return math.gcd(p, q) == 1

    def getE(self):
        for i in range (self.phi, 1 -1):
            if (is_coprime(i, p, q)):
                e = i
        print (e)
        return e

    def __init__(self, L):
        # Initializes
        self.p, self.q = generatePrimes(L)
        self.e = getE()

        # Calculates n, phi, and d
        self.n = p * q
        self.phi = (p - 1) * (q - 1)
        self.d = pow(self.e, -1, self.phi)

    # Encrypts using e and n
    def encrypt(self, m):
        return pow(m, self.e, self.n)

    # Decrypts using d and n
    def decrypt(self, c):
        return pow(c, self.d, self.n)

