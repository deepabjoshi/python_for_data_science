print("Hello universe!")

programming_languages = 'Python', 'Java', 'C++', 'Perl', 'Ruby'
print(programming_languages)
print(type(programming_languages))

for language in programming_languages:
    print(language, type(language))

STR = "I am a game"
s = "A game"

def f():
    print(STR)
    print(s)
    str = "abc"
    print(str)
    # Following statement generates and Error at line 15 that local variable
    # referenced before assignment.
    # s = "xyz"
    # print(s)

f()
# In the following statement str refers to class str
print(str)
print(s)


# Mutability test
x = 1
def test():
    x = 2
test()
print(x) # x = 1

x = 1
def test():
    global x
    x = 2
test()
print(x) # x = 2

x = [1]
def test():
    x = [2]
test()
print(x) # x = [1]

x = [1]
def test():
    global x
    x = [2]
test()
print(x) # x = [2]

x = [1]
def test():
    x[0] = 2
test()
print(x) # x = [2]


