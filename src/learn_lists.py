# Lists are mutable
a = [1, 2, 3, 4]
b = a
print("a = ", a)
print("b = ", b)
a[0] = 100
print("a = ", a)
print("b = ", b)

# Lists are not copied above, but if one is deleted using del operator, other remains
del a
# Following statement gives a not defined error
# print("a = ", a)
print("b = ", b)

# Looping through a list
for i in b:
    print(i)

# List membership with in
print("1 in b =", 1 in b)
print("100 in b =", 100 in b)

# Finding length of a list
print("len([1, 2, 3, 4, 5]) =", len([1, 2, 3, 4, 5]))

# List methods
r = b.append(5)
print("b = {0}, r = {1}".format(b, r))
x = b.pop()
print("b = {0}, x = {1}".format(b, x))
r = b.extend([2, 6, 7])
print("b = {0}, r = {1}".format(b, r))
print("b.index(6) =", b.index(6))
print("b.index(2) =", b.index(2))
# Following statement raise ValueError
# print("b.index(6, 0, 4) =", b.index(6, 0, 4))
# print("b.index(1) =", b.index(1))
r = b.append([7, 8, 9])
print("b = {0}, r = {1}".format(b, r))
print("b.count(2) =", b.count(2))
print("b.count(7) =", b.count(7))
r = b.insert(15, 10)
print("b = {0}, r = {1}".format(b, r))
r = b.insert(1, 1)
print("b = {0}, r = {1}".format(b, r))
r = b.remove(2)
print("b = {0}, r = {1}".format(b, r))
r = b.remove([7, 8, 9])
print("b = {0}, r = {1}".format(b, r))
r = b.reverse()
print("b = {0}, r = {1}".format(b, r))
r = b.sort()
print("b = {0}, r = {1}".format(b, r))

a = b.copy()
print("a =", a)
print("a == b", a == b)
b.clear()
print("After clearing, a == b", a == b)
print("a =", a, ", b =", b)

