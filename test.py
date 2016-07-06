import functools


def a(p,q):
    return p + q + 1


def b(func, p):
    return functools.partial(func, p,p)


c = b(a, 10)
print c()
