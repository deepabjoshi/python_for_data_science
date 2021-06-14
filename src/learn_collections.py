from collections import *

# ChainMap
d1 = {'a': 1, 'c': 2}
d2 = {'x': 3, 'd': 4, 'e': 5}
c = ChainMap(d1, d2)
print(dir(c))
for k, v in c.items():
    print(k, v)
print('c.maps =', c.maps)
print('c.parents =', c.parents)
e = c.new_child()
print('e.maps =', e.maps)
print('e.parents =', e.parents)
print('e.maps[0] =', e.maps[0])
print('e.maps[1] =', e.maps[1])
print('e.maps[2] =', e.maps[2])
print('e.maps[-1] =', e.maps[-1])
f = e.new_child()
print('f.maps =', f.maps)
print('f.parents =', f.parents)
print()

c['y'] = 100
e['z'] = 200
f['w'] = 300
print('c.maps =', c.maps)
print('e.maps =', e.maps)
print('f.maps =', f.maps)
print('f.keys() =', f.keys())
print()

print("f['x'] =", f['x'])
# deleting x from c, e or f gives KeyError
del d2['x']
del f['w']
print('c.maps =', c.maps)
print('e.maps =', e.maps)
print('f.maps =', f.maps)
for k, v in f.items():
    print(k, v)
print()


# Counter objects
lcnt = Counter()
print(dir(lcnt))
for l in 'hello world':
    lcnt[l] += 1
print(lcnt)
print("lcnt['h'] =", lcnt['h'])
print("lcnt['p'] =", lcnt['p'])
print()

print('Elements:', list(lcnt.elements()))
print('Top 2:', lcnt.most_common(2))
lcnt[' '] = 0
print(lcnt)
del lcnt[' ']
print(lcnt)
lcnt.subtract('hello')
print('After subracting hello:', lcnt)
lcnt.update('low')
print('After adding low:', lcnt)
print()

cnt1 = Counter('abcde')
cnt2 = Counter('efghi')
print('Counter1, counter2 =', cnt1, cnt2)
cnt3 = cnt1 + cnt2
print('cnt1, cnt2, cnt3 =', cnt1, cnt2, cnt3)
print('cnt1 & cnt2 =', cnt1 & cnt2)
print('cnt1 | cnt2 =', cnt1 | cnt2)
cnt2['e'] = 3
print('After adding e to cnt2: cnt1 & cnt2 =', cnt1 & cnt2)
print('After adding e to cnt2: cnt1 | cnt2 =', cnt1 | cnt2)
print('cnt1 - cnt2 =', cnt1 - cnt2)
print('cnt2 - cnt1 =', cnt2 - cnt1)
cnt1['!'] = -5
print('cnt1 =', cnt1)
print('-cnt1 =', -cnt1)
print('+cnt1 =', +cnt1)
print()


# deque objects
