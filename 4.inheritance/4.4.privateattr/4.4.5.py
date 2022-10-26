import functools


def class_log(lst):
    def adder(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            lst.append(func.__name__)
            return func(*args, **kwargs)

        return wrapper

    def log_methods(cls):
        methods = {key: value for key, value in cls.__dict__.items() if callable(value)}
        for key, value in methods.items():
            setattr(cls, key, adder(value))

        return cls

    return log_methods


vector_log = []  # наименование (vector_log) в программе не менять!


@class_log(vector_log)
class Vector:
    def __init__(self, *args):
        self.__coords = list(args)

    def __getitem__(self, item):
        return self.__coords[item]

    def __setitem__(self, key, value):
        self.__coords[key] = value


v = Vector(1, 2, 3)
v[0] = 10
print(vector_log)
