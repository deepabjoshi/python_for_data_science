from collections import *
import re

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
d1 = deque([1, 2, 3, 4])
print('d1 =', d1)
d1.append(1)
d1.appendleft(-1)
print('d1 =', d1)
print('d1.count(1) =', d1.count(1))
print('d1.count(5) =', d1.count(5))
d1.extend([5, 6, 7, 8])
d1.extendleft([-2, -3, -4])
print('d1 =', d1)
d1.insert(4, 0)
d1.pop()
d1.popleft()
print('d1 =', d1)
print('d1.index(0) =', d1.index(0))
d1.remove(1)
print('d1 =', d1)
try:
    d1.remove(100)
except ValueError as e:
    print('d1.remove(100): ', e)
d1.rotate(2)
print('d1 =', d1)
d1.rotate(-2)
print('d1 =', d1)
d2 = deque(maxlen=4)
print('d2 =', d2)
d2.extend(['a', 'b', 'c', 'd'])
print('d2 =', d2)
d2.reverse()
print('d2 =', d2)
d2.append('e')
print('d2 =', d2)
d2.appendleft('x')
print('d2 =', d2)
d3 = d2.copy()
print('d3 =', d3)


# defaultdict
print(dir(defaultdict))
riddle = """1 was a racehorse
2 was 12
111 race
2112
"""
s = defaultdict(int)
for r in riddle:
    s[r] +=1
print('Letter in riddle:', sorted(s.items()))

w = defaultdict(list)
riddle_one_line = re.subn('\n', ' ', riddle)
print(riddle_one_line)
for word in riddle_one_line[0].split(' '):
    w[len(word)].append(word)
print('Words in riddle:', sorted(w.items()))

u = defaultdict(set)
for word in riddle_one_line[0].split(' '):
    u[len(word)].add(word)
print('Unique words in riddle:', sorted(u.items()))

uc = defaultdict(lambda: defaultdict(int))
for word in riddle_one_line[0].split(' '):
    uc[len(word)][word] += 1
print('Unique words in riddle with counts:', sorted(uc.items()))


# OrderedDict()
print(dir(OrderedDict))
o = OrderedDict()
for line in riddle.split('\n'):
    for word in line.split(' '):
        if word in o:
            o[word] += 1
        else:
            o[word] = 1
    print(o)
o.move_to_end('was')
print(o)
o.popitem()
print(o)
del o['1']
print(o)
o['1'] = 100
print(o)

# Not doing UserDict, UserList and UserString right now.

