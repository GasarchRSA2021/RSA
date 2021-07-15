"""
Program to test out rsa_encryption.py
"""

# Imports rsa_encryption.py to use the file's functions etc -> can call module by rsa instead of rsa_encryption
import rsa_encryption as rsa

# Asks for p, q, e, and m
p = int(input("Enter p to be encrypted: "))
q = int(input("Enter q to be encrypted: "))
e = int(input("Enter e to be encrypted: "))
m = int(input("Enter the plaintext to be encrypted: "))

# Creates an object called test with given variables
test = rsa.RSA(p, q, e, m)

# Prints plaintext, ciphertext, and decrypted ciphertext
print("\nPlaintext: ", m)

c = test.encrypt(m)
print("Ciphertext: ", c)

d = test.decrypt(c)
print("Decrypted text: ", d)
