class BookStudy:
    def __init__(self, name, author, year):
        self.name = name
        self.author = author
        self.year = year

    def __hash__(self):
        return hash((self.name.lower(), self.author.lower()))

    def __eq__(self, other):
        return hash(self) == hash(other)


lst_in = [
    'Python; Балакирев С.М.; 2020',
    'Python ООП; Балакирев С.М.; 2021',
    'Python ООП; Балакирев С.М.; 2022',
    'Python; Балакирев С.М.; 2021',
]
lst_bs = []
for i in lst_in:
    lst_bs.append(BookStudy(i.split(";")[0], i.split(";")[1], i.split(";")[2]))

unique_books = len(set(lst_bs))
print(unique_books)