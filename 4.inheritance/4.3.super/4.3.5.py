class SoftList(list):
    def __getitem__(self, item):
        try:
            return super().__getitem__(item)
        except IndexError:
            return False

sl = SoftList("python")
sl[0] # 'p'
print(sl[-1]) # 'n'
print(sl[6]) # False
sl[-7] # False