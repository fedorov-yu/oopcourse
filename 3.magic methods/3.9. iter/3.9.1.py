class Person:
    def __init__(self, fio, job, old, salary, year_job):
        self.fio = fio
        self.job = job
        self.old = old
        self.salary = salary
        self.year_job = year_job
        self.lst = list(self.__dict__.values())

    def __getitem__(self, item):
        if 0 <= item < len(self.lst):
            return self.lst[item]
        else:
            raise IndexError('неверный индекс')

    def __setitem__(self, key, value):
        if 0 <= key < len(self.lst):
            self.lst[key] = value
        else:
            raise IndexError('неверный индекс')

    def __iter__(self):
        self.__value = -1
        return self

    def __next__(self):
        if self.__value < len(self.lst)-1:
            self.__value += 1
            return self.lst[self.__value]
        else:
            raise StopIteration


pers = Person('Гейтс Б.', 'бизнесмен', 61, 1000000, 46)
pers[0] = 'Балакирев С.М.'
for v in pers:
    print(v)
pers[5] = 123  # IndexError
