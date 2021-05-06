import timeit
from collections import ChainMap


def create_dict(size):
    # Example: dictionary comprehension
    curr_dict = {i: str(i) for i in range(1, size + 1)}
    # print(curr_dict)
    return curr_dict


def swap_key_val_1(curr_dict):
    new_dict = {}
    for k, v in curr_dict.items():
        new_dict[v] = k
    # print(new_dict)
    return new_dict


def swap_key_val_2(curr_dict):
    # Example: dictionary comprehension
    new_dict = {v: k for k, v in curr_dict.items()}
    # print(new_dict)
    return new_dict


def swap_key_val_3(curr_dict):
    new_dict = dict(zip(curr_dict.values(), curr_dict.keys()))
    # print(new_dict)
    return new_dict


def get_int_val(t):
    return int(t[1])


size = 10000
curr_dict = create_dict(size)
d1 = timeit.timeit('swap_key_val_1(curr_dict)', number=100, globals=globals())
print('d1 =', d1)
d2 = timeit.timeit('swap_key_val_2(curr_dict)', number=100, globals=globals())
print('d2 =', d2)
d3 = timeit.timeit('swap_key_val_3(curr_dict)', number=100, globals=globals())
print('d3 =', d3)

# Result: swap_key_val_3 performs best.

my_dict = create_dict(20)
print('my_dict =', my_dict)
swap_dict = swap_key_val_3(my_dict)
print('swap_dict =', swap_dict)

# Example: dictionary modification
for k, v in my_dict.items():
    if k % 5 == 0:
        my_dict[k] = v * 2
print('modified my_dict =', my_dict)

# Example: dictionary deletion incorrect
# Gives RuntimeError since we are deleting keys during iteration. Alternate way is given below.
# for k, v in swap_dict.items():
#     if v % 5 == 0:
#         del swap_dict[k]
# Example: dictionary deletion correct
for k in list(swap_dict.keys()):
    if swap_dict[k] % 5 == 0:
        del swap_dict[k]
print('modified swap_dict =', swap_dict)

# Example: dictionary sorting - reverse sorting by key
for k in sorted(my_dict, reverse=True):
    print(k, my_dict[k])

print()
# Example: dictionary sorting by value
swap_dict['1'] = 100
for k, v in sorted(swap_dict.items(), key=lambda item: item[1]):
    print(k, v)

print()
# Example: dictionary sorting using function
for k, v in sorted(my_dict.items(), key=get_int_val):
    print(k, v)

# Example: iterating dictionary destructively using popitem()
while True:
    try:
        print(f'Dictionary length: {len(swap_dict)}')
        item = swap_dict.popitem()
        # Do something with item here...
        print(f'{item} removed')
    except KeyError:
        print('The dictionary has no item now...')
        break

# Example: ChainMap for iterating through two or more dictionaries
d1 = {'a': 1, 'c': 2}
d2 = {'x': 3, 'd': 4, 'e': 5}
print('d1 =', d1)
print('d2 =', d2)
chained_dicts = ChainMap(d1, d2)
for k, v in chained_dicts.items():
    print(k, v)
