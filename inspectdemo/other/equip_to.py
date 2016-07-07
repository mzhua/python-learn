import inspect


def equip_to(cls):
    def f(fn):
        if inspect.isfunction(fn):
            setattr(cls, fn.func_name, fn)
        elif inspect.isclass(fn):
            for name in dir(fn):
                attr = getattr(fn, name)
                if inspect.ismethod(attr):
                    print name
                    if name == '__init__':
                        name += fn.__name__ + '__'
                        print name
                    setattr(cls, name, attr.im_func)
                    if name == '__init__' + fn.__name__ + '__':
                        attr.im_func(cls)
        return fn

    return f
