class Record:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def __checker(self, key):
        if not isinstance(key, int) or key > len(list(self.__dict__.values())) - 1:
            raise IndexError('неверный индекс поля')

    def __getitem__(self, key):
        self.__checker(key)
        return getattr(self, list(self.__dict__.keys())[key])

    def __setitem__(self, key, value):
        self.__checker(key)
        setattr(self, list(self.__dict__.keys())[key], value)


r = Record(pk=1, title='Python ООП', author='Балакирев')
print(r.pk) # 1
print(r.title) # Python ООП
print(r.author) # Балакирев
r[0] = 2 # доступ к полю pk
r[1] = 'Супер курс по ООП' # доступ к полю title
r[2] = 'Балакирев С.М.' # доступ к полю author
print(r[0], r[1], r[2]) # Супер курс по ООП
print(r.title)
r[3]  # генерируется исключение IndexError
