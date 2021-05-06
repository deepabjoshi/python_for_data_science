l = ['a', 'b', 'c', 'd']
h = dict.fromkeys(l)
print("h =", h)
h = dict.fromkeys(l, 10)
print("h =", h)

print("h.get('a') =", h.get('a'))
print("h.get('x') =", h.get('x'))
print("h['a'] =", h['a'])
# Following statement gives KeyError
# print("h['x'] =", h['x'])

print("h.items() =", h.items())
print("h.keys() =", h.keys())
print("h.values() =", h.values())

print("h.pop('a') =", h.pop('a'), ", h =", h)
# Following statement gives KeyError
# print("h.pop('x') =", h.pop('x'), ", h =", h)
print("h.pop('x') =", h.pop('x', -1), ", h =", h)

h['a'] = 100
print("h =", h)

hc = dict.fromkeys(h, 200)
print("hc =", hc)
t = hc.popitem()
print("hc =", hc, ", t =", t)
hc = hc.clear()
print("hc =", hc)
hc = {}
# The following statement gives KeyError
# t = hc.popitem()
hc['a'] = 10
v = hc.setdefault('x', 10)
print("hc =", hc, ", v =", v)
v = h.setdefault('b', -1)
print("h =", h, ", v =", v)
hc.update(h)
print("hc =", hc)
del hc['d']
print("hc =", hc)

print("Value of x is %(x)d" %hc)