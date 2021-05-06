my_list = [1, 2, 3, 4, 5, 6]
a, *b, c = my_list
print(a, b, c)

d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}
d3 = {**d1, **d2}
print(d3)

# If the same key is present, latest value is used
d4 = {'a': 1, 'b': 3}
d5 = {'b': 2, 'd': 4}
d6 = {**d4, **d5}
print(d6)

# Unpacking string
str = 'Hello world!'
print(*str)

# Matrix transpose using unpacking
matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12]]
print(*matrix)
print(list(zip(*matrix)))