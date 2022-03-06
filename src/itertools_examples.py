import itertools
import operator


K = 10

# Infinite iterators - count, cycle, repeat
for i in itertools.count(5):
    print(i)
    if i >= K:
        break
print()

for i, e in enumerate(itertools.cycle([11, 22, 33, 44])):
    print(e)
    if i >= K:
        break
print()

for i, e in enumerate(itertools.repeat(5)):
    print(e)
    if i >= K:
        break
print()


for p in itertools.accumulate(range(1, 5), operator.mul):
    print(p)
print()

print(list(itertools.chain('ABCD', 'EFGH')))
print(list(itertools.combinations('ABCD', 2)))
print(list(itertools.combinations_with_replacement('ABCD', 2)))
print(list(itertools.permutations('ABCD', 2)))
print(list(itertools.product('ABC')))
print(list(itertools.product('ABC', 'DEF')))
print()

print(list(itertools.compress('ABCDEFG', [1, 0, 1, 1])))
print(list(itertools.compress('ABCDEFG', [True, False, False, True, True, False, True, True])))
print()

print(list(itertools.dropwhile(lambda x: x <= 'D', 'ABCDEFGC')))
print(list(itertools.takewhile(lambda x: x <= 'D', 'ABCDEFGC')))
print(list(itertools.filterfalse(lambda x: x <= 'D', 'ABCDEFGC')))
print(list(itertools.filterfalse(lambda x: x % 2, range(10))))
print()

print(list(itertools.groupby('AABBBCCCDDAAA')))
print(list(k for k, g in itertools.groupby('AABBBCCCDDAAA')))
print(list(list(g) for k, g in itertools.groupby('AABBBCCCDDAAA')))
print(list((k, len(list(g))) for k, g in itertools.groupby('AABBBCCCDDAAA')))
print(dir(itertools._grouper))
print()

print(list(itertools.islice('ABCDEFGH', 2)))
print(list(itertools.islice('ABCDEFGH', 2, None)))
print(list(itertools.islice('ABCDEFGH', 1, None, 2)))

print(list(itertools.starmap(lambda x, y: x * y, [(1, 3), (2, 5), (100, 100)])))
print(list(itertools.starmap(lambda x: x * 3, [(1,), (2,), (100,)])))
print(list(itertools.starmap(lambda x, y, z: x + y + z, [(1, 2, 3), (4, 5, 6), (100, 100, 100)])))

print(list(itertools.tee(range(10), 3)))
i1, i2, i3 = itertools.tee(range(10), 3)
print(list(i1), list(i2), list(i3))
print(list(itertools.zip_longest('ABCD', 'xy', fillvalue='-')))
