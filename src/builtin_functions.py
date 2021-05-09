"""
This covers the builtin functions whose meaning is not easily clear by looking
at their name. abs(), len() etc. are obvious.
"""

# any() and all()
l = [True, False]
print(l)
print("any(l) = ", any(l))
print("all(l) = ", all(l))
m = ['a', 'b', 'c', 'd']
print(m)
print("all(m) = ", all(m))
n = ['a', 'b', 'c', '']
print(n)
print("all(n) = ", all(n))


# bin(), hex(), oct(), type()
print('type(bin(10)) =',  type(bin(10)))
print('type(oct(10)) =',  type(oct(10)))
print('type(hex(10)) =',  type(hex(10)))
for i in range(0, 17):
    print(i, bin(i), oct(i), hex(i))


# bool()
v = 0
w = None
x = 1
y = 'a'
z = ''
print(v, '  bool(v) =', bool(v))
print(w, '  bool(w) =', bool(w))
print(x, '  bool(x) =', bool(x))
print(y, '  bool(y) =', bool(y))
print(z, '  bool(z) =', bool(z))


# callable()
print('callable(len) =', callable(len))
print('callable(x) =', callable(x))


# chr() and ord()
print('int(0x2208) =', int(0x2208))
print('chr(int(0x2208)) =', chr(int(0x2208)))
print('ord(\'∈\') =', ord('∈'))


# dir()
print('dir():', dir())
print('dir({}):', dir({}))
import timeit
print('dir(timeit):', dir(timeit))
print('dir() after importing timeit:', dir())


# divmod()
q, r = divmod(10, 3)
print('divmod(10, 3) =', q, r)


# enumerate()
print('m =', m)
print('enumerate(m) =', enumerate(m))
print('list(enumerate(m)) =', list(enumerate(m)))


# eval()
x = 1
print('eval(\'x+1\') =', eval('x + 1'))


# exec()
print('exec(\'x + 1\'):', exec('x + 1'))


# filter()
l1 = [True, False, 0, 1, 10, 20, 30]
def f1(x):
    return True

def f2(x):
    return int(x) > 10

l2 = list(filter(f1, l1))
l3 = list(filter(None, l1))
l4 = list(filter(f2, l1))
l5 = list(filter(lambda x: x > 20, l1))
print('l1 =', l1)
print('l2 =', l2)
print('l3 =', l3)
print('l4 =', l4)
print('l5 =', l5)


# globals() and locals()
a = 10
b = 20
def test(p1, p2):
    c = 30
    print('globals() =', globals())
    print('locals() =', locals())
test(a, b)


# iter(), len()
l = [1, 2, 3, 4, 5]
print('len(l) =', len(l), l)
it = iter(l)
print(1, next(it))
print(2, next(it))
print(3, next(it))
print(4, next(it))
print(5, next(it))
# Generates StopIteration exception
# print(6, next(it))

# zip() and unzip like functionality
# Please note that zip forms tuple only until shortest iterable is exhausted
numbers = [1, 2, 3, 4]
letters = ['a', 'b', 'c', 'd', 'e']
operators = ['+', '-', '*', '/']
triples = zip(numbers, letters, operators)
print('triples object =', triples)
print('triples =', list(triples))
pairs = zip(numbers, letters)
numbers, letters = zip(*pairs)
print('numbers =', numbers)
print('letters =', letters)


# sum() and map(), reversed()
l1 = [1, 2, 3, 4, 5]
l2 = [10, 20, 30, 40, 50]
print(l1)
print('sum of squares of l1 =', sum(map(lambda x: x * x, l1)))
print(l2)
print('parallel sum of l1 and l2 =', list(map(lambda x, y: x + y, l1, l2)))
print('reversed l1 =', list(reversed(l1)))


# round()
print('round(3.14159, 4) =', round(3.14159, 4))
print('round(0.5) =', round(0.5))
print('round(-0.5) =', round(-0.5))


# slice()
s = slice(0, 11, 2)
print('s =', s)
str = 'Hello world!'
print('slice of str =', str[s])