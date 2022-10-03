class Player:
    def __init__(self, name, old, score):
        self.name = name
        self.old = old
        self.score = score

    def __bool__(self):
        return int(self.score) > 0

    def __repr__(self):
        return f"{self.name} -- {self.score}"





lst_in = ['Балакирев; 34; 2048',
          'Mediel; 27; 0',
          'Влад; 18; 9012',
          'Nina P; 33; 0']
players = [Player(i.split(";")[0], i.split(";")[1], i.split(";")[2]) for i in lst_in]
players_filtered = list(filter(lambda x: bool(x), players))
print(players_filtered)