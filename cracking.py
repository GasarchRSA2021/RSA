import rsa_encryption as rsa
import factoring as f
import time

def countTime(func, t):
    start = time.time()
    func(t)
    end = time.time()
    return end-start

r = rsa.RSA(1000)
n, e = r.public()

print(countTime(f.pollardrho, 8051))
print(countTime(f.quadSieve, 8051))
print(countTime(f.trivial, 8051))