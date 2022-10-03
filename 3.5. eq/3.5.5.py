class FileAcceptor:
    def __init__(self, *args):
        self.lst = args

    def __call__(self, filename):
        return filename.split('.')[-1] in self.lst

    def __add__(self, other):
        new_lst = list(set(self.lst + other.coords))
        return self.__class__(*new_lst)

    def get_items(self):
        return tuple(self.lst)


acceptor1 = FileAcceptor("jpg", "jpeg", "png")
acceptor2 = FileAcceptor("png", "bmp")
acceptor12 = acceptor1 + acceptor2  # ("jpg", "jpeg", "png", "bmp")

filenames = ["boat.jpg", "ans.web.png", "text.txt", "www.python.doc", "my.ava.jpg", "forest.jpeg", "eq_1.png",
             "eq_2.xls"]
acceptor_images = FileAcceptor("jpg", "jpeg", "png")
acceptor_docs = FileAcceptor("txt", "doc", "xls")
ac = acceptor_docs + acceptor_images

filenames = list(filter(ac, filenames))
print(filenames)
