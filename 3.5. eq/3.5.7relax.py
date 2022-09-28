class Body:
    def __init__(self, name, ro, volume):
        self.name = name if type(name) == str else ''
        self.ro = ro if type(ro) in (int, float) else None
        self.volume = volume if type(volume) in (int, float) else None

    def __weight(self):
        return self.ro * self.volume

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__weight() == other.__weight()
        if isinstance(other, (int, float)):
            return self.__weight() == other

    def __lt__(self, other):
        if isinstance(other, self.__class__):
            return self.__weight() < other.__weight()
        if isinstance(other, (int, float)):
            return self.__weight() < other

    def __le__(self, other):
        if isinstance(other, self.__class__):
            return self.__weight() <= other.__weight()
        if isinstance(other, (int, float)):
            return self.__weight() <= other
