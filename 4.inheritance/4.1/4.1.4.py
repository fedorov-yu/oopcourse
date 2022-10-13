class Singleton:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "instance"):
            cls.instance = super().__new__(cls)
        return cls.instance


class Game(Singleton):
    def __init__(self, name):
        if not hasattr(self, 'name'):
            self.name = name


# class Singleton:
#     __instance = None
#     __instance_base = None
#
#     def __new__(cls, *args, **kwargs):
#         if cls == Singleton:
#             if not cls.__instance_base:
#                 cls.__instance_base = super().__new__(cls)
#             return cls.__instance_base
#
#         if not cls.__instance:
#             cls.__instance = super().__new__(cls)
#         return cls.__instance
#
#





