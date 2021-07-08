plaintext = int(input("Enter the plaintext to be encrypted: "))

p = 2
q = 7
e = 5
n = p*q
phi = (p - 1)*(q - 1)
print("phi = ", phi)

def encrypt(plaintext):
    return pow(plaintext, e, n)

print("Plaintext: ", plaintext)

ciphertext = encrypt(plaintext)
print("Ciphertext: ", ciphertext)

d = pow(e, -1, phi)
print("d =", d)

def decrypt(ciphertext):
    return pow(ciphertext, d, n)

decryptedtext = decrypt(ciphertext)
print("Decrypted text: ", decryptedtext)