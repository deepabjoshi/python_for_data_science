# For exception hierarchy, look at https://docs.python.org/3.6/library/exceptions.html

class B(Exception):
    pass

class C(B):
    pass

class D(C):
    pass


for cls in [B, C, D]:
    try:
        print(cls, dir(cls))
        raise cls()
    except D:
        print("D")
    except C:
        print("C")
    except B:
        print("B")