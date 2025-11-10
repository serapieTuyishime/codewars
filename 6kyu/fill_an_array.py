# Following on from Part 1, part 2 looks at some more complicated array contents.
#
# So let's try filling an array with...
#
# ...square numbers
# The numbers from 1 to n*n
#
# const squares = n => ???
# squares(5) // [1, 4, 9, 16, 25]
# ...a range of numbers
# A range of numbers starting from start and increasing by step
#
# const range = (n, start, step) => ???
# range(6, 3, 2) // [3, 5, 7, 9, 11, 13]
# ...random numbers
# A bunch of random integers between min and max
#
# const random = (n, min, max) => ???
# random(4, 5, 10) // [5, 9, 10, 7]
# ...prime numbers
# All primes starting from 2 (obviously)...
#
# const primes = n => ???
# primes(6) // [2, 3, 5, 7, 11, 13]

import random
import itertools


def squares(n):
    return [n ** 2 for n in range(1, n + 1)]


def num_range(n, start, step):
    return [i for i in range(start, (start + step * n), step)]


def rand_range(n, mn, mx):
    return [random.randint(mn, mx) for _ in range(n)]


def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def primes(n):
    result = []
    i = 0
    while True:
        if is_prime(i):
            result.append(i)
        if len(result) == n:
            break
        i += 1
    return result
