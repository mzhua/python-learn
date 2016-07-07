import inspect


def equip_to(cls):
    def f(fn):
        if inspect.isfunction(fn):
            setattr(cls, fn.func_name, fn)
        elif inspect.isclass(fn):
            for name in dir(fn):
                attr = getattr(fn, name)
                if inspect.ismethod(attr):
                    if name == '_setup':
                        name += '_' + fn.__name__
                    setattr(cls, name, attr.im_func)
                    if name == '_setup_' + fn.__name__:
                        attr.im_func(cls)
        return fn

    return f
