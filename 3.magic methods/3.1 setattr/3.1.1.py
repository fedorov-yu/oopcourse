class Book:
    def __init__(self, title='', author='', pages=0, year=0):
        self.title = title
        self.author = author
        self.pages = pages
        self.year = year

    def __setattr__(self, key, value):
        if key == 'title' or key == 'author':
            if type(value) == str:
                object.__setattr__(self, key, value)
            else:
                raise TypeError("Неверный тип присваиваемых данных.")
        elif key == 'pages' or key == 'year':
            if type(value) == int:
                object.__setattr__(self, key, value)
            else:
                raise TypeError("Неверный тип присваиваемых данных.")


book = Book('Python ООП', 'Сергей Балакирев', 123, 2022)
book2 = Book('Python ООП', 'Сергей Балакирев', 'qwe', 2022)
print(book2.__dict__)
