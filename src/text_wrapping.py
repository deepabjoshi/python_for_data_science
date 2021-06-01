import textwrap


riddle = """1 is a racehorse
2 is 12
    111 race
2112"""

riddle2 = """    1 is a racehorse
    2 is 12
    111 race
    2112"""

print('Textwrap width 8:')
for l in textwrap.wrap(riddle, width=8):
    print(l)
print()
print('Textwrap width 7:')
for l in textwrap.wrap(riddle, width=7):
    print(l)
print()
print('Textwrap width 100:')
for l in textwrap.wrap(riddle, width=100):
    print(l)
print()

print('Fill width 8:')
print(textwrap.fill(riddle, width=8))
print('Fill width 7:')
print(textwrap.fill(riddle, width=7))
print('Fill width 100:')
print(textwrap.fill(riddle, width=100))
print()

print('Shorten width 10:')
print(textwrap.shorten(riddle, width=10))
print('Shorten width 100:')
print(textwrap.shorten(riddle, width=100))
print()

print('Dedent: riddle')
print(textwrap.dedent(riddle))
print()
print('Dedent: riddle2')
print(textwrap.dedent(riddle2))
print()

print('Indent: riddle')
print(textwrap.indent(riddle, '--'))
print()
print('Indent: riddle2')
print(textwrap.indent(riddle2, '=='))
print()
