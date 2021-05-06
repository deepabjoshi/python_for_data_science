# Example: chained comparison
a = 1
b = 2
c = 2
print (a, b, c, a < b == c)

s1, s2, s3 = None, '', 'Hi'
print(s1, s2, s3, s1 or s2 or s3)

print("'x' < 'y' < 'z' < 'w' =", 'x' < 'y' < 'z' < 'w')
print("'x' < 'y' < 'z' =", 'x' < 'y' < 'z')

# Example: comparing sequences
# Raises TypeError
# str1 = '[1, 2, 3] < (1, 2, 4)'
# print(str1, '=', eval(str1))
str2 = '[1, 2, 3] < [1, 2, 4]'
print(str2, '=', eval(str2))
# The following works, because mixed numeric types are compared according to their numerical value,
str3 = '(1, 2, 3) == (1.0, 2.0, 3.0)'
print(str3, '=', eval(str3))
str4 = "(1, 2, 3) == ('1', '2', '3')"
print(str4, '=', eval(str4))