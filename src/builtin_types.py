import sys

# Information about precision and internal representation of floating point numbers for the machine
# on which program is running
print(sys.float_info)


# Complex types
c = complex(2, 4)
print(c, c.real, c.imag, c.conjugate())
print(c.__dir__())


# Bitwise operations on integers
x = 5
y = 12
print('x =', x, 'y =', y)
print('x | y =', x | y)
print('x & y =', x & y)
print('x ^ y =', x ^ y)
print('x << 2 =', x << 2)
print('x >> 1 =', x >> 1)
print('~x =', ~x)
print('x.bit_length() =', x.bit_length(), 'y.bit_length() =', y.bit_length())


# Floats
x = 1.5
y = 2.33333333333333333333333333333333
z = 2.0
print('x =', x, 'x.is_integer() =', x.is_integer(), 'x.as_integer_ratio() =', x.as_integer_ratio())
print('y =', y, 'y.is_integer() =', y.is_integer(), 'y.as_integer_ratio() =', y.as_integer_ratio())
print('z =', z, 'z.is_integer() =', z.is_integer(), 'z.as_integer_ratio() =', z.as_integer_ratio())


# Hashing numeric types - information about how numeric types are hashed
print(sys.hash_info)
# Hashing for immutable sequence types
t = (1, 2, 3)
w = (1, 2)
print('t =', t, 'hash(t) =', hash(t))
print('w =', w, 'hash(w) =', hash(w))


# set operations
s1 = {'a', 'b', 'c', 'd', 'a'}
s2 = {'d', 'e', 'f'}
s3 = {'a'}
print('s1 =', s1)
print('s2 =', s2)
print('s3 =', s3)
print('s1.isdisjoint(s2) =', s1.isdisjoint(s2))
print('s3.isdisjoint(s2) =', s3.isdisjoint(s2))
print('s3.issubset(s1) =', s3.issubset(s1))
print('s3.issubset(s2) =', s3.issubset(s2))
print('s1.issuperset(s2) =', s1.issuperset(s2))
print('s1.issuperset(s3) =', s1.issuperset(s3))
s4 = {'d', 'e', 'f'}
print('s4 =', s4)
print('s3 < s1 =', s3 < s1)
print('s4 < s2 =', s4 < s2)
print('s4 <= s2 =', s4 <= s2)
print('s1.difference(s2) =', s1.difference(s2))
print('s1.symmetric_difference(s2) =', s1.symmetric_difference(s2))
print('s1.union(s2) =', s1.union(s2))
print('s1.intersection(s2) =', s1.intersection(s2))
print('s1 =', s1)
print('s2 =', s2)
print('s3 =', s3)
print('s4 =', s4)
# Follwoing statement gives TypeError: unhashable type: 'list'
# s5 = {['a']}
print(s3.copy())


# modules
print('Symbol table of sys: ', sys.__dict__)