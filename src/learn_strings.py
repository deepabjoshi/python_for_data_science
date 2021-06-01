str = 'abcd'

print("str =", str)
print()

print("'abab'.find('ab') =", 'abab'.find('ab'))
print("'abab'.find('xy') =", 'abab'.find('xy'))
print("'abab'.index('ab') =", 'abab'.index('ab'))
# Following statement raises ValueError
# print("'abab'.index('xy') =", 'abab'.index('xy'))
print("'abab'.rfind('ab') =", 'abab'.rfind('ab'))
print("'abab'.rfind('xy') =", 'abab'.rfind('xy'))
print("'abab'.rindex('ab') =", 'abab'.rindex('ab'))
# Following statement raises ValueError
# print("'abab'.rindex('xy') =", 'abab'.rindex('xy'))
print("str.endswith('cd') =", str.endswith('cd'))
print("str.startswith('cd') =", str.startswith('cd'))
print("'abcdab'.count('ab') =", 'abcdab'.count('ab'))
print("'abcdab'.count('ab', 0, 4) =", 'abcdab'.count('ab', 0, 4))
print()

print("str.isalnum() =", str.isalnum())
print("'123a'.isalnum() =", '123a'.isalnum())
print("str.isalpha() =", str.isalpha())
print("'123a'.isalpha() =", '123a'.isalpha())
print("str.isdigit() =", str.isdigit())
print("'1234'.isdigit() =", '1234'.isdigit())
print("'123a'.isdigit() =", '123a'.isdigit())
print("str.islower() =", str.islower())
print("str.isupper() =", str.isupper())
print("'ABC'.isupper() =", 'ABC'.isupper())
print("'Abc'.isupper() =", 'Abc'.isupper())
print("str.istitle() =", str.istitle())
print("'ABC Def'.istitle() =", 'ABC Def'.istitle())
print("'Abc Def'.istitle() =", 'Abc Def'.istitle())
print("str.isspace() =", str.isspace())
print("'python program'.isspace() =", 'python program'.isspace())
print("' '.isspace() =", ' '.isspace())
print("'\t'.isspace() =", '\t'.isspace())
print("''.isspace() =", ''.isspace())
print()

print("'!' + str.zfill(8) + '!' = ", '!' + str.zfill(8) + '!')
print("'!' + str.ljust(8) + '!' = ", '!' + str.ljust(8) + '!')
print("'!' + str.ljust(8, '-') + '!' = ", '!' + str.ljust(8, '-') + '!')
print("'!' + str.rjust(8) + '!' = ", '!' + str.rjust(8) + '!')
print("'!' + str.rjust(8, '-') + '!' = ", '!' + str.rjust(8, '-') + '!')
print("str.center(8) =", str.center(8))
print("'abcde'.center(8, '#') =", 'abcde'.center(8, '#'))
print("'ab\tcd'.expandtabs() =", 'ab\tcd'.expandtabs())
print("'ab\tcd'.expandtabs(16) =", 'ab\tcd'.expandtabs(16))
print("'--abcdef----'.lstrip('-') =", '--abcdef----'.lstrip('-'))
print("'--abcdef----'.rstrip('-') =", '--abcdef----'.rstrip('-'))
print("'--abcdef----'.strip('-') =", '--abcdef----'.strip('-'))
print()

print("'hello world!'.lower() =", 'hello world!'.lower())
print("'hello world!'.upper() =", 'hello world!'.upper())
print("'hello world!'.title() =", 'hello world!'.title())
print("'hello world!'.capitalize() =", 'hello world!'.capitalize())
print("'Hello World!'.swapcase() =", 'Hello World!'.swapcase())
print()

print("', '.join(['aa', 'bb', 'cc', 'dd']) =", ', '.join(['aa', 'bb', 'cc', 'dd']))
print("'ab|cd|ef'.partition('|') =", 'ab|cd|ef'.partition('|'))
print("'ab|cd|ef'.rpartition('|') =", 'ab|cd|ef'.rpartition('|'))
print("'ab|cd|ef'.partition(' ') =", 'ab|cd|ef'.partition(' '))
print("'abxycdxyefxygh'.replace('xy', '|') =", 'abxycdxyefxygh'.replace('xy', '|'))
print("'abxycdxyefxygh'.replace('xy', '|', 2) =", 'abxycdxyefxygh'.replace('xy', '|', 2))
print("'ab|cd|ef|gh'.split('|') =", 'ab|cd|ef|gh'.split('|'))
print("'ab|cd|ef|gh'.split('|', 2) =", 'ab|cd|ef|gh'.split('|', 2))
print("'ab|cd|ef|gh'.rsplit('|') =", 'ab|cd|ef|gh'.rsplit('|'))
print("'ab|cd|ef|gh'.rsplit('|', 2) =", 'ab|cd|ef|gh'.rsplit('|', 2))
print()

text ="""
Hello World!
Have a great day!!
"""
print(text)
print(text.splitlines())

intab = 'eol'
outtab = '301'
t = str.maketrans(intab, outtab)
print("'hello world'.translate(t) =", 'hello world'.translate(t))

# String formatting
# More on formatting at https://docs.python.org/3.6/library/string.html
print('{0}, {1}, {2}'.format('a', 'b', 'c'))
print('{0}{1}{0}'.format('und', 'ergro'))
print('x = {x}, y = {y}'.format(x=10, y=20))
point = {'x': 10, 'y': 20}
print('x = {x}, y = {y}'.format(**point))
coord = (3, 5)
print('X: {0[0]};  Y: {0[1]}'.format(coord))
riddle = """
%d is a %shorse
%d is %d
%d race
%d
""" % (1, 'race', 2, 12, 111, 2112)
print(riddle)

print('abcd abcd.isidentifier() =', 'abcd'.isidentifier())
print('_x1 _x1.isidentifier() =', '_x1'.isidentifier())
print('#$ #$.isidentifier() =', '#$'.isidentifier())
print()


# helper functions
import string
print("string.capwords('hello world!') =", string.capwords('hello world!'))
