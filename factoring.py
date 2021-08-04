"""
Quad Sieve Factoring
https://en.wikipedia.org/wiki/Quadratic_sieve
"""
import math
import numpy as np
import helper
import sympy as sy

# Quad Sieve uses difference of squares to find factors
def quadSieve(N, B=19):
    a = math.ceil(math.sqrt(N))  # find the starting testing value (ceiling of the square root of N)
    primes = helper.genNPrimes(B)  # use the genNPrimes() function to generate a list of B primes
    numArr = []  # keeps track of the a values
    vectorArr = np.array([])  # keeps track of the exponent values
    parityArr = np.array([])  # keeps track of the parity values

    while len(parityArr) <= B + 1:
        bFactor, expArr = (helper.bFactorable(primes, (a ** 2) % N))  # finds if factorisable and exp array

        # adds to numArr, vectorArr, and parityArr
        if (bFactor == True):
            numArr.append(a)
            if a == math.ceil(math.sqrt(N)):
                vectorArr = expArr
                parityArr = helper.parityVector(expArr)
            else:
                vectorArr = np.vstack([vectorArr, expArr])
                parityArr = np.vstack([parityArr, helper.parityVector(expArr)])

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

    return math.gcd(int(x), N)

def pollardrho(N, f="x**2+1"):
    def g(formula=f, **kwargs):
        expr = sy.sympify(formula)
        return expr.evalf(subs=kwargs)

    x1 = 2
    y = 2
    d = 1
    while d == 1:
        x = g(x=x1)
        y = g(x=g(x=y))
        d = math.gcd(abs(int(x-y)), N)
    return d

def fermat(N):
    a = math.ceil(math.sqrt(N))
    b2 = a**2 - N
    while (not(math.sqrt(b2).is_integer())):
        a += 1
        b2 = a ** 2 - N
        print(a, b2)
    return a - math.sqrt(b2)

def trivial(N):
    possibleFactors = list(sy.primerange(2, math.floor(math.sqrt(N))))

    for i in reversed(possibleFactors):
      if N % i == 0:
         p = i
         q = N/p
         return p, q