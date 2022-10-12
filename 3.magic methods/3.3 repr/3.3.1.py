import sys


class Book:
    def __init__(self, *args):
        self.title = args[0]
        self.author = args[1]
        self.pages = args[2]

    def __str__(self):
        return f"Книга: {self.title}; {self.author}; {self.pages}"


lst_in = list(map(str.strip, sys.stdin.readlines()))
book = Book(*lst_in)
print(book)
