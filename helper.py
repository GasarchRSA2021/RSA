"""
Functions that can help with other programs
"""
import numpy as np
import sympy


# Generating Primes
# Creates a list of primes and adds when cannot be divided by other primes
def genNPrimes(N):
    primes = []
    i = 2  # i represents values testing to be prime

    # Generates primes until N primes are found
    while (len(primes) < N):
        flag = False  # if flag is True, then it means we found a prime that i divided into
        for p in primes:
            if (i % p == 0):
                i += 1
                flag = True  # i divided into one of the primes
                break
        if flag == False:
            primes.append(i)  # add to primes if flag was hit (if i divided by a prime)
    return primes  # returns a list of B primes


# Determines if x is factorable given the primes
def bFactorable(primes, x):
    i = 0  # i increases based on the prime we are looking at
    arr = [0] * len(primes)  # arr is an array of length B that counts how many times each prime is multiplied

    while x != 1 and i != len(primes):
        tempX = x / primes[i]  # create a temp variable that divides by the prime
        if tempX.is_integer():  # if the temp variable divides completely (int), then the ith prime divides x at
            x = tempX  # least once
            arr[i] += 1  # only go to the next prime when we know that the prime is not a factor
        else:
            i += 1
    if (x != 1):  # if the number we are looking at hasn't been divided
        return (False, None)  # completely by the given primes, return false and no array
    else:
        return (True, arr)  # otherwise, return true and the exponent array


# Takes the exponent vector and creates a vector of the parities
def parityVector(arr):
    parityArr = []
    for i in arr:
        parityArr.append(i % 2)
    return parityArr


# Finds the dependent vectors by taking out the independent vectors
def findDependentVectors(parityArr):
    dep = set(range(0, len(parityArr)))  # create a set that contains all values from 0 to B
    ind = set()  # create an empty set for independent vectors
    _, inds = sympy.Matrix(parityArr).T.rref()  # find the independent vectors
    if (len(inds) == len(parityArr)):  # if all the rows are independent, then there aren't dep vectors
        return {}
    for i in inds:
        temp = np.delete(parityArr, i, 0)  # take out rows one by one to see how many are independent
        _, tempInds = sympy.Matrix(temp).T.rref()  # find independent vectors now
        if len(tempInds) != len(temp):
            ind.add(i)  # add row numbers that are independent
    return dep.difference(ind)  # return the set that contains all row numbers except those that are independent
