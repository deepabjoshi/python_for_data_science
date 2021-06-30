"""
learn about numerical and mathematical modules like math, statistics, random etc.
"""


import random

print(dir(random))
print()

# Default seed is current system time
print([random.random() for j in range(0, 10)])
print([random.random() for j in range(0, 10)])
print()

# Same seed produces same sequence
for i in range(0, 4):
    random.seed(1)
    print([random.random() for j in range(0, 10)])
print()

# Functions for integers
print('Random integers up to 10:', [random.randrange(10) for j in range(0, 10)])
print('Random integers from 1 to 10:', [random.randrange(1, 11) for j in range(0, 10)])
print('Random integers from 2 to 10 step 2:', [random.randrange(2, 11, 2) for j in range(0, 10)])
print('Random integers from 5 to 15:', [random.randint(5, 15) for j in range(0, 10)])
print()

# Functions for sequences
letters = ['a', 'b', 'c', 'p', 'q', 'r', 'x', 'y', 'z']
print('Random choice:', [random.choice(letters) for j in range(0, 5)])
c = random.choices(letters, k=6)
print('Random choices:', c)
random.shuffle(c)
print('Shuffle:', c)
print('Random sample no replacement:', random.sample(letters, 6))
print()

# Real valued distibutions
print('Random distribution:', [random.random() for j in range(0, 10)])
print('Uniform distribution:', [random.uniform(1.0, 2.0) for j in range(0, 10)])
# Default mode is mid range for triangular
print('Triangular distribution:', [random.triangular(1.0, 2.0) for j in range(0, 10)])
print('Betavariate distribution:', [random.betavariate(1.0, 2.0) for j in range(0, 10)])
print('Expovariate distribution:', [random.expovariate(0.5) for j in range(0, 10)])
print('Gammavariate distribution:', [random.gammavariate(1.0, 2.0) for j in range(0, 10)])
print('Gauss distribution:', [random.gauss(0.5, 1) for j in range(0, 10)])
print('Normalvariate distribution:', [random.normalvariate(0.5, 1) for j in range(0, 10)])
print('Lognormvariate distribution:', [random.lognormvariate(0.5, 1) for j in range(0, 10)])
# There are three other real valued distributions - vonmisesvariate, paretovariate, weibullvariate
