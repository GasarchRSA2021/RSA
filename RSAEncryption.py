"""
Program for encryption and decryption given p, q, and e
"""

# Creates a class for encrypting and decrypting given p, q, e, and m
# Stores inside of object
class RSA:
    def __init__(self, p, q, e):
        # Initializes
        self.p = p
        self.q = q
        self.e = e

        # Calculates n, phi, and d
        self.n = p*q
        self.phi = (p - 1) * (q - 1)
        self.d = pow(self.e, -1, self.phi)

    # Encrypts using e and n
    def encrypt(self, m):
        return pow(m, self.e, self.n)

    # Decrypts using d and n
    def decrypt(self, c):
        return pow(c, self.d, self.n)
