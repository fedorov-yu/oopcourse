class IteratorAttrs:
    def __iter__(self):
        yield from self.__dict__.items()


class SmartPhone(IteratorAttrs):
    def __init__(self, model: str, size: tuple[float | int, float | int], memory: int):
        self.model = model
        self.size = size
        self.memory = memory


phone = SmartPhone('1', (1, 1), 100)
for attr, value in phone:
    print(attr, value)
