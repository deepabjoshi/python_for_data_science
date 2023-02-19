import random

# If no seed is provided, system time is used as seed.
random.seed()

print(random.randbytes(5))

# Integers
for i in range(0, 10):
    print(random.randrange(15))
print()
for i in range(0, 10):
    print(random.randrange(1, 8, 2))
print()
print(random.randint(2, 5))
print(random.getrandbits(4))
print(random.getrandbits(5))
print()

# Sequences
seq = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
wt = [2, 1, 2, 2, 1, 5, 5, 3, 2, 2, 1, 2]
for i in range(0, 5):
    print(random.choice(seq))
print()
print(random.choices(seq, k=5))
print(random.choices(seq, wt, k=5))
seq_shuff = seq.copy()
print(seq_shuff)
random.shuffle(seq_shuff)
print(seq_shuff)
print(random.sample(seq, 3))
print()

# Real valued distributions
print(random.random())
print(random.uniform(2.4, 5.6))
for i in range(20):
    print(random.gauss(0.0, 0.8))
