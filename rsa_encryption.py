"""
Program for encryption and decryption given p, q, and e
"""
import helper

# Creates a class for encrypting and decrypting given p, q, e, and m
# Stores inside of object
class RSA:
    def __init__(self, L):
        # Calculates n, phi, and d
        self.p, self.q = helper.generatePrimes(L)
        self.n = self.p * self.q
        self.phi = (self.p - 1) * (self.q - 1)
        self.e, self.d = helper.getED(self.phi)

    # Encrypts using e and n
    def encrypt(self, m):
        return pow(m, self.e, self.n)

    # Decrypts using d and n
    def decrypt(self, c):
        return pow(c, self.d, self.n)

    def public(self):
        return self.n, self.e

