"""
Quad Sieve Factoring
https://en.wikipedia.org/wiki/Quadratic_sieve
"""
import math
import random

import numpy as np
import helper
import sympy as sy

# Quad Sieve uses difference of squares to find factors
def quadSieve(N, B=100000):
    flag = False

    a = math.ceil(math.sqrt(N))  # find the starting testing value (ceiling of the square root of N)
    primes = helper.genNPrimes(B)  # use the genNPrimes() function to generate a list of B primes
    numArr = []  # keeps track of the a values
    vectorArr = np.array([])  # keeps track of the exponent values
    parityArr = np.array([])  # keeps track of the parity values

    while True:
        bFactor, expArr = (helper.bFactorable(primes, (a ** 2) % N))  # finds if factorisable and exp array

        # adds to numArr, vectorArr, and parityArr
        if (bFactor == True):
            numArr.append(a)
            if not(flag):
                vectorArr = expArr
                parityArr = helper.parityVector(expArr)
                flag = True
            else:
                vectorArr = np.vstack([vectorArr, expArr])
                parityArr = np.vstack([parityArr, helper.parityVector(expArr)])
                print(vectorArr)

                dep = helper.findDependentVectors(parityArr)  # finds the dependent vectors
                if len(dep) > 0:  # if there are dependent vectors, then stop looking for more vectors
                    break
        a += 1  # test next value

    prod = 1
    exp = 1
    sumexparr = np.zeros(B)

    # for all dependent vectors in the matrix, multiply the corresponding numbers together
    # as well as sum the exponent vectors
    for d in dep:
        prod *= numArr[d] % N
        sumexparr += vectorArr[d]

    sumexparr /= 2
 
    # calculate the "Y" value
    for i in range(len(sumexparr)):
        exp *= primes[i] ** sumexparr[i]

    # find the first factor using the diff of squares
    x = prod - exp

    #print (prod, exp, x)

    p = math.gcd(int(x), N)
    q = N/p

    return (p, q)

def pollardrho(N):
    x = 2
    y = 2
    c = 1
    d = 1

    def f(x, c=c, N=N, exp=2):
        return (x ** 2 + c) % N

    while d == 1:
        x = f(x)
        y = f(f(y))


        if (d == N):
            x = (random.randint(0, 2) % (N - 2))
            y = x
            c = (random.randint(0, 1) % (N - 1))

        else:
            d = math.gcd(abs(x - y), N)

    return d, N/d

def fermat(N):
    a = math.ceil(math.sqrt(N))
    b2 = a**2 - N
    print(a, b2)
    while (not(math.sqrt(b2).is_integer())):
        a += 1
        b2 = a ** 2 - N

    p = a - math.sqrt(b2)
    q = N/p

    return (p, q)

def trivial(N):
    for i in range(2, math.ceil(math.sqrt(N))+1):
      if N % i == 0:
         p = i
         q = N/p
         return p, q

def trivial2(N):
    possibleFactors = list(sy.primerange(2, math.floor(math.sqrt(N))))

    for i in reversed(possibleFactors):
      if N % i == 0:
         p = i
         q = N/p
         return p, q