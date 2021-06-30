import copy

l1 = [1, 2, 3]
l2 = ['a', 'b', 'c', l1]
l3 = l2.copy()
l4 = copy.copy(l2)
l5 = copy.deepcopy(l2)
print(l1)
print(l2)
print(l3)
print(l4)
print(l5)
l1.append(4)
print(l1)
print(l2)
print(l3)
print(l4)
print(l5)
