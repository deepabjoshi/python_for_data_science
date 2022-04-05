from pathlib import Path

# Not looking at os.path since much of the functionality is similar to pathlib
# lchmod is not available on linux

p = Path('.')
print(dir(p))
print(p)

print(Path.cwd())
print(p.cwd())
print(p.home())
print(p.stat())
print(p.exists())
print(Path('/home/DEEPA').exists())
print(Path('~/books').expanduser())

print(p.glob('*.py'))
for f in p.glob('learn_*.py'):
    print(f)

print(p.group())
print(p.is_dir())
print(Path('./learn_lists.py').is_dir())
print(Path('./learn_lists.py').is_file())
print(Path('./learn_lists.py').is_mount())
print(Path('./learn_lists.py').is_symlink())
print(Path('./learn_lists.py').is_socket())
print(Path('./learn_lists.py').is_fifo())
print(Path('./learn_lists.py').is_block_device())
print(Path('./learn_lists.py').is_char_device())

for f in Path('..').iterdir():
    if f.is_dir():
        print(f)

d = Path('/tmp/pathtest/deepa')
d.mkdir(parents=True)
print(oct(d.stat().st_mode))
d.chmod(0o500)
print(oct(d.stat().st_mode))
k = Path('/tmp/pathtest/kedar')
k.symlink_to('/tmp/pathtest/deepa')
print(oct(k.stat().st_mode))
print(k.is_symlink())
print(k.readlink())
print(k.owner())
f = d.rename('/tmp/pathtest/dark')
print(f)
n = f.replace('/tmp/pathtest/deepa')
print(n)
print(k)
print(k.resolve())
k.unlink()
d.rmdir()
Path('/tmp/pathtest').rmdir()

print('--------------------')
r = Path('..')
for rf in r.glob('learn_*.py'):
    print(rf)
print('--------------------')
for rf in r.rglob('learn_*.py'):
    print(rf)
print()

dir(p.parents)
print(p, 'name =', p.name)
print(p, 'parts =', p.parts)
print(p, 'parent =', p.parent)
print(p, 'drive =', p.drive)
print(p, 'root =', p.root)
print(p, 'anchor =', p.anchor)
p = p.resolve()
print(p, 'name =', p.name)
print(p, 'parts =', p.parts)
print(p, 'parent =', p.parent)
print(p, 'drive =', p.drive)
print(p, 'root =', p.root)
print(p, 'anchor =', p.anchor)
print(p.as_uri())
print(p.match('*data*'))
print(p.match('*data*/src'))
print(p.match('*science/src'))

print(Path('./data.tar.gz').suffix)
print(Path('./data.tar.gz').suffixes)
print(Path('./data.tar.gz').stem)
print(Path('/home/deepa').joinpath('data.tar.gz'))
print(p.match('data'))