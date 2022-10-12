class DataBase:

    def __init__(self, path):
        self.path = path
        self.dict_db = dict()

    def write(self, record):
        self.dict_db.setdefault(record, []).append(record)

    def read(self, pk):
        obj = tuple(filter(lambda x: x[0].pk == pk, self.dict_db.values()))
        return obj


class Record:
    ID = 0

    def __init__(self, fio, descr, old):
        self.pk = self.ID
        Record.ID += 1
        self.fio = fio
        self.descr = descr
        self.old = old

    def __hash__(self):
        return hash((self.fio.lower(), self.old))

    def __eq__(self, other):
        return hash(self) == hash(other)

    def __ne__(self, other):
        return hash(self) != hash(other)

    def __repr__(self):
        return f"{self.fio} ---- {self.descr} ---- {self.old}"


lst_in = ['Балакирев С.М.; программист; 33',
          'Кузнецов Н.И.; разведчик-нелегал; 35',
          'Суворов А.В.; полководец; 42',
          'Иванов И.И.; фигурант всех подобных списков; 26',
          'Балакирев С.М.; преподаватель; 33'
          ]

db = DataBase('path')
for j, i in enumerate(lst_in, start=0):
    db.write(Record(i.split(";")[0], i.split(";")[1], i.split(";")[2]))
    db.read(j)
print(db.dict_db)
