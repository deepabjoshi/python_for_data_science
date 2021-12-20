"""
Various ways to find all primes up to a number n.
This also contains examples of comprehension, how to time a part of code.
Times various algorithms. The last one is based on a mathematical proof that
every prime number > 3 can be represented as 6k-1 or 6k+1.
Find example of generator
"""
import timeit


def check_prime(i, primes):
    for p in primes:
        if p ** 2 > i:
            return True
        if i % p == 0:
            return False
    return True


def sieve_of_eratosthenus(n):
    if n < 2:
        return []
    sieve = [2]
    # Create sieve - Saving some space by not adding any even number except 2
    for i in range(3, n + 1, 2):
        sieve.append(i)

    idx = 1
    while idx < len(sieve) - 1:
        # Example: list comprehension with condition
        sieve[idx + 1:] = [i for i in sieve[idx + 1:] if i % sieve[idx] != 0]
        idx += 1

    return sieve


def using_primes(n):
    if n < 2:
        return []
    elif n < 3:
        return [2]
    primes = [2, 3]
    lo = primes[-1] + 2
    hi = min(primes[-1]**2, n)
    while lo <= n:
        new_primes = []
        for i in range(lo, hi + 1, 2):
            if check_prime(i, primes):
                new_primes.append(i)
        lo = hi + 2
        hi = min(hi ** 2, n)
        primes.extend(new_primes)
    return primes


def using_6k(n):
    if n < 2:
        return []
    elif n < 3:
        return [2]
    primes = [2, 3]
    for i in range(5, n + 1, 6):
        if check_prime(i, primes):
            primes.append(i)
        if check_prime(i + 2, primes):
            primes.append(i + 2)
    return primes


def prime_generator(n):
    yield 2
    yield 3
    i = 5
    primes = [2, 3]
    while i <= n:
        if check_prime(i, primes):
            primes.append(i)
            yield i
        if check_prime(i + 2, primes):
            primes.append(i + 2)
            yield i + 2
        i += 6


def using_generator(n):
    # Example: generator, list comprehension
    primes = [i for i in prime_generator(n)]
    return primes


# print(sieve_of_eratosthenus(100))
# print(using_primes(100))
# print(using_6k(100))
# print(using_generator(100))

# Example: timeit
s = timeit.timeit('sieve_of_eratosthenus(100000)', number=1, globals=globals())
print('s =', s)
p = timeit.timeit('using_primes(100000)', number=1, globals=globals())
print('p =', p)
k = timeit.timeit('using_6k(100000)', number=1, globals=globals())
print('k =', k)
g = timeit.timeit('using_generator(100000)', number=1, globals=globals())
print('g =', g)