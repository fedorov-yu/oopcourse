class Morph:
    def __init__(self, *args):
        self.lst = list(args)
        # print(self.lst)

    def add_word(self, word):
        if word not in self.lst:
            self.lst.append(word)

    def get_words(self):
        return tuple(self.lst)

    def __eq__(self, other):
        if isinstance(other, str):
            return other.lower() in self.lst


dict_words = [Morph('связь', 'связи', 'связью', 'связи', 'связей', 'связям', 'связями', 'связях'),
              Morph('формула', 'формулы', 'формуле', 'формулу', 'формулой', 'формул', 'формулам', 'формулами',
                    'формулах'),
              Morph('вектор', 'вектора', 'вектору', 'вектором', 'векторе', 'векторы', 'векторов', 'векторам',
                    'векторами', 'векторах'
                    ),
              Morph('эффект', 'эффекта', 'эффекту', 'эффектом', 'эффекте', 'эффекты', 'эффектов', 'эффектам',
                    'эффектами', 'эффектах'
                    ),
              Morph('день', 'дня', 'дню', 'днем', 'дне', 'дни', 'дням', 'днями', 'днях')]
# print(dict_words[0].get_words())

text = input()
counter = 0
text = text.replace('.', '').replace(',', '').split()
for i in text:
    for words in dict_words:
        if i == words:
            print(i)
            counter += 1
print(counter)
