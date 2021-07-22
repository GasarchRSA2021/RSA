"""
Program for encryption and decryption given p, q, and e
"""
import sympy
import math
from random import randint

# Creates a class for encrypting and decrypting given p, q, e, and m
# Stores inside of object
class RSA:
    def __init__(self, L):
        # Calculates n, phi, and d
        self.p, self.q = self.generatePrimes(L)
        self.n = self.p * self.q
        self.phi = (self.p - 1) * (self.q - 1)
        self.e, self.d = self.getED()

    def generatePrimes(self, L):
        p = sympy.randprime(2, L)
        q = sympy.randprime(2, L)
        return (p, q)

    def is_coprime(e, p, q):
        return math.gcd(p, q) == 1

    def getED(self):
        e = randint(1, self.phi)
        while True:
            try:
                if math.gcd(e, self.phi) != 1:
                    raise(ValueError)
                else:
                    d = pow(e, -1, self.phi)
                    return (e, d)
            except:
                e+=1

    # Encrypts using e and n
    def encrypt(self, m):
        return pow(m, self.e, self.n)

    # Decrypts using d and n
    def decrypt(self, c):
        return pow(c, self.d, self.n)

