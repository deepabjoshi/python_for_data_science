import re


def match_and_print(pattern, str, flags=0):
    m = re.match(pattern, str, flags)
    if m:
        print('match pattern =', pattern, 'str =', str, m, m[0])
    else:
        print('match pattern =', pattern, 'str =', str, 'Not found')


def search_and_print(pattern, str, flags=0):
    m = re.search(pattern, str, flags)
    if m:
        print('search pattern =', pattern, 'str =', str, m, m[0])
    else:
        print('search pattern =', pattern, 'str =', str, 'Not found')


def findall_and_print(pattern, str, flags=0):
    m = re.findall(pattern, str, flags)
    if m:
        print('findall pattern =', pattern, 'str =', str, m)
    else:
        print('findall pattern =', pattern, 'str =', str, 'Not found')


print(dir(re))

riddle = """1 was a racehorse
2 was 12
111 race
2112
"""

# search, match and findall
# search and match return a match object, while findall returns a list of string
# match finds at the beginning of the string
# search finds first location anywhere in the string
# findall finds all occurances
match_and_print('abc', 'abcdef')
search_and_print('abc', 'abcdef')
print()
match_and_print('def', 'abcdef')
search_and_print('def', 'abcdef')
print()
match_and_print('^2', riddle)
search_and_print('^2', riddle)
print()
match_and_print('^2', riddle, re.M)
search_and_print('^2', riddle, re.M)
print()
match_and_print('e$', riddle, re.M)
search_and_print('e$', riddle, re.M)
print()

# Flags
# Multi-line
findall_and_print('^2', riddle)
findall_and_print('^2', riddle, re.M)
findall_and_print('e$', riddle, re.M)
print()
# Ignorecase
match_and_print('abc', 'Abcdefabcdef')
search_and_print('abc', 'Abcdefabcdef')
findall_and_print('abc', 'Abcdefabcdef')
match_and_print('abc', 'Abcdefabcdef', re.I)
search_and_print('abc', 'Abcdefabcdef', re.I)
findall_and_print('abc', 'Abcdefabcdef', re.I)
print()
# Dotall
findall_and_print('e.', riddle, re.M)
findall_and_print('e.', riddle, re.M | re.S)
print()
match_and_print('abc', 'abcdef', re.DEBUG)
match_and_print('def', 'abcdef', re.DEBUG)
print()
# Not checking re.LOCALE right now


# Utility functions
m = re.fullmatch('abc', 'abcdef')
if m:
    print('abc fully matched with abcdef')
else:
    print('abc not fully matched with abcdef')
m = re.fullmatch('abc', 'abc')
if m:
    print('abc fully matched with abc')
else:
    print('abc not fully matched with abc')
print()

s = re.split('x.', 'abcx-defx+abcx-def')
print('Splitting on x. ', s)
s = re.split('(x.)', 'abcx-defx+abcx-def')
print('Splitting on (x.) ', s)
fi = re.finditer('x.', 'abcx-defx+abcx-def')
print('Finditer:')
for s in fi:
    print(s, s[0])
print()

str = re.sub('\n', ';', riddle)
print(str)
t = re.subn('\n', ';', riddle)
print(t)
print()

print('Escaping:', re.escape('abcx-defx+abcx-def'), '\n')

# Regular expression objects
regexp = re.compile('x.')
print('Pattern: ', regexp.pattern)
print('Groups:', regexp.groups, '\tGroup index:', regexp.groupindex)
s = regexp.search('abcx-defx+abcx-def')
print('Search result: ', s, s[0])
regexp = re.compile('(?P<id>[^x]+)(?P<sep>x.)')
print('Pattern: ', regexp.pattern)
print('Groups:', regexp.groups, '\tGroup index:', regexp.groupindex)
s = regexp.search('abcx-defx+abcx-def')
print('Search result: ', s, s[0])
print()


# Match objects
df = 'Deepa Joshi, Apoorv Mhaswade, Rujuta Mhaswade, Kedar Mhaswade'
m = re.search('((?P<fn>[A-Z][a-z]*)[ ]*(?P<ln>[A-Z][a-z]*))', df)
print('Searching names:')
print(m)
print(m.groups())
print(m.groupdict())
for i in range(0, len(m.groups()) + 1):
    print(m.group(i), m[i], m.start(i), m.end(i), m.span(i))
print(m.pos, m.endpos, m.lastindex, m.lastgroup)
print()

regexp = re.compile("""(([A-Z][a-z]*)  # First name
                       [ ]*  # Spaces
                       ([A-Z][a-z]*)) # Last name""", re.VERBOSE)
m = regexp.search(df, 12, 50)
print('Searching names in positions 12-50:')
print(m)
print(m.groups())
print(m.groupdict())
for i in range(0, len(m.groups()) + 1):
    print(m.group(i), m[i], m.start(i), m.end(i), m.span(i))
print(m.pos, m.endpos, m.lastindex, m.lastgroup)
print()


# Exception conditions
try:
    m = re.search('[a-z', 'abcdef-abcdef')
except re.error as e:
    print(e)
    print('--', e.args, '|', e.colno, '|', e.lineno, '|', e.msg, '|', e.pattern, '|', e.pos)
print()

# Escaped literals
findall_and_print(r'\Apy', 'py py')
findall_and_print('\bpy', 'py py')
findall_and_print(r'\bpy', 'py py')
findall_and_print(r'\Bpy', 'py py')
findall_and_print(r'\Bpy', 'pypy')
findall_and_print(r'\d', '१')
findall_and_print(r'\d', '१', re.ASCII)
findall_and_print(r'\D', '₹ १')
findall_and_print(r'\s', '₹ १')
findall_and_print(r'\S', '₹ १')
findall_and_print(r'\w+', 'abc-def-ghi')
findall_and_print(r'\W+', 'abc--def-ghi')
findall_and_print(r'.on\Z', ' on non python')
findall_and_print(r'\\', 'a\c\d\e\tf')
findall_and_print(r'[^\\]', 'a\c\d\e\tf')
findall_and_print(r'[\\\t]', 'a\c\d\e\tf')
findall_and_print(r'[^\\\t]', 'a\c\d\e\tf')
print()


# Number of matches
print('Pattern =', '((?P<fn>[A-Z][a-z]*)[ ]*(?P<ln>[A-Z][a-z]*),?[ ]*){2}')
m = re.search('((?P<fn>[A-Z][a-z]*)[ ]*(?P<ln>[A-Z][a-z]*),?[ ]*){2}', df)
print(m[0], m.groups())
print('Pattern =', '((?P<fn>[A-Z][a-z]*)[ ]*(?P<ln>[A-Z][a-z]*),?[ ]*){3}')
m = re.search('((?P<fn>[A-Z][a-z]*)[ ]*(?P<ln>[A-Z][a-z]*),?[ ]*){3}', df)
print(m[0], m.groups())
print('Pattern =', '((?P<fn>[A-Z][a-z]*)[ ]*(?P<ln>[A-Z][a-z]*),?[ ]*){4}')
m = re.search('((?P<fn>[A-Z][a-z]*)[ ]*(?P<ln>[A-Z][a-z]*),?[ ]*){4}', df)
print(m[0], m.groups())
print('Pattern =', '((?P<fn>[A-Z][a-z]*)[ ]*(?P<ln>[A-Z][a-z]*),?[ ]*){3,5}')
m = re.search('((?P<fn>[A-Z][a-z]*)[ ]*(?P<ln>[A-Z][a-z]*),?[ ]*){3,5}', df)
print(m[0], m.groups())
print('Pattern =', '((?P<fn>[A-Z][a-z]*)[ ]*(?P<ln>[A-Z][a-z]*),?[ ]*){3,5}?')
m = re.search('((?P<fn>[A-Z][a-z]*)[ ]*(?P<ln>[A-Z][a-z]*),?[ ]*){3,5}?', df)
print(m[0], m.groups())
print()


# Lazy evaluations
search_and_print(r'[A-Z][a-z]*', 'Hello World')
search_and_print(r'[A-Z][a-z]*?', 'Hello World')
findall_and_print(r'[A-Z][a-z]*?', 'Hello World')
search_and_print(r'[A-Z][a-z]+', 'Hello World')
search_and_print(r'[A-Z][a-z]+?', 'Hello World')
findall_and_print(r'[A-Z][a-z]+?', 'Hello World')
search_and_print(r'[A-Z][a-z]?', 'Hello World')
search_and_print(r'[A-Z][a-z]??', 'Hello World')
findall_and_print(r'[A-Z][a-z]??', 'Hello World')
print()


# Groups
findall_and_print(r'(([a-z]{3})-\2)', 'abc-abc-def-def-wxyz-wxyz')
findall_and_print(r'(([a-z]{3,5})-\2)', 'abc-abc-def-def-wxyz-wxyz')
findall_and_print(r'(([a-z]{3})-\2)', 'abc-abc-def-def-wxyz-wxyza')
findall_and_print(r'(([a-z]{3,5})([,-|])\2)', 'abc-abc-def|def-wxyz,wxyz')
findall_and_print(r'(([a-z]{3,5})([,-|])\2)', 'abc-abc,abc-def|def-wxyz,wxyz')
print()

# (?...) variations
findall_and_print(r'((?P<id>[a-z]{3,5})(?:[,-|])(?P=id))', 'abc-abc-def|def-wxyz,wxyz')
findall_and_print(r'(([a-z]{3,5})(?:[,-|])\2)', 'abc-abc-def|def-wxyz,wxyz')
# The (?=...) is called lookahead assertion. It doesn't consume the string
findall_and_print(r'(([a-z]{3,5})([,-|])(?=\2))', 'abc-abc,abc-def|def-wxyz,wxyz')
findall_and_print(r'Hello (?=world)', 'Hello Hello world, Hello py')
findall_and_print(r'Hello (?=world)', 'Hello world Hello world, Hello py')
# The (?!...) is called negative lookahead assertion. It doesn't consume the string
findall_and_print(r'Hello (?!world)', 'Hello Hello world, Hello py')
# Positive lookbehind assertion (?<=...)
findall_and_print(r'(?<=Hello) [Ww]orld.', 'world- Hello World, Hello world+')
# Negative lookbehind assertion (?<!...)
findall_and_print(r'(?<!Hello) [Ww]orld.', ' world- Hello World, Hello world+')
# name/id yes-no pattern matching
# yes pattern is working as given in the doc, but no pattern isn't
findall_and_print(r'(abc)(?(1)(def)|(wxyz))', 'abcdefwxyz')
findall_and_print(r'(abc)(?(1)(def)|(wxyz))', 'defwxyz')
findall_and_print(r'(<)?(\w+@\w+(?:\.\w+)+)(?(1)>|$)', '<user@host.com>')
findall_and_print(r'(<)?(\w+@\w+(?:\.\w+)+)(?(1)>|$)', 'user@host.com')
findall_and_print(r'(<)?(\w+@\w+(?:\.\w+)+)(?(1)>|$)', 'user@host.com>')  # No match as expected
findall_and_print(r'(<)?(\w+@\w+(?:\.\w+)+)(?(1)>|$)', '<user@host.com')  # Matches but it shouldn't

