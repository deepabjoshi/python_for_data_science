import functools
import timeit


# No examples of the following since they are more relevant for object oriented python:
# cached_property, lru_cache, total_ordering, partial_method, singledispatchmethod
# Other concepts - singledispatch, update_wrapper, wraps
# These methods can be found in https://docs.python.org/3.9/library/functools.html


# lru_cache and cache are similar. cache is same as lru_cache(maxsize=None)
# Generally, use cache because it makes code clean. Use lru_cache only when it is necessary to limit cache size.
@functools.cache
def factorial(n):
    return n * factorial(n - 1) if n else 1


def factorial_nocache(n):
    return n * factorial(n - 1) if n else 1


base_hex = functools.partial(int, base=16)
base_hex.__doc__ = 'Convert base 16 string to an int'
print(base_hex.__doc__)
print(base_hex('0x1a'), '\n')

print(functools.reduce(lambda x, y: x + y, [1, 2, 3, 4, 5]))
print(functools.reduce(min, [1, 2, 3, 4, 5]))
print(functools.reduce(lambda x, y: x + y, ['a', 'b', 'c', 'd']), '\n')

f5 = timeit.timeit('factorial(5)', number=1000, globals=globals())
print('f5 =', f5)
n5 = timeit.timeit('factorial_nocache(5)', number=1000, globals=globals())
print('n5 =', n5)
f15 = timeit.timeit('factorial(15)', number=1000, globals=globals())
print('f15 =', f15)
n15 = timeit.timeit('factorial_nocache(15)', number=1000, globals=globals())
print('n15 =', n15)
f25 = timeit.timeit('factorial(25)', number=1000, globals=globals())
print('f25 =', f25)
n25 = timeit.timeit('factorial_nocache(25)', number=1000, globals=globals())
print('n25 =', n25)

