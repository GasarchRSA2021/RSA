"""
Program to test out rsa_encryption.py
"""

# Imports rsa_encryption.py to use the file's functions etc -> can call module by rsa instead of rsa_encryption
import rsa_encryption as rsa

# Creates an object called test with given variables
test = rsa.RSA(1000)

# Prints plaintext, ciphertext, and decrypted ciphertext
print("\nPlaintext: ", m)

c = test.encrypt(m)
print("Ciphertext: ", c)

d = test.decrypt(c)
print("Decrypted text: ", d)
