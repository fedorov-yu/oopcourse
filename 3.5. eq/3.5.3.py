stich = ["Я к вам пишу – чего же боле?",
         "Что я могу еще сказать?",
         "Теперь, я знаю, в вашей воле",
         "Меня презреньем наказать.",
         "Но вы, к моей несчастной доле",
         "Хоть каплю жалости храня,",
         "Вы не оставите меня."]
stich_v2 = []
for row in stich:
    stich_v2.append(row.replace('–', '').replace('.', '').replace('?', '').replace('!', '').replace(';', '').split())


# print(stich_v2)


class StringText:
    def __init__(self, lst_words, ):
        self.lst_words = lst_words

    def __len__(self):
        return len(self.lst_words)

    def __gt__(self, other):
        if isinstance(other, self.__class__):
            return len(self) > len(other)

    def __lt__(self, other):
        if isinstance(other, self.__class__):
            return len(self) < len(other)

    def __ge__(self, other):
        if isinstance(other, self.__class__):
            return len(self) >= len(other)

    def __le__(self, other):
        if isinstance(other, self.__class__):
            return len(self) <= len(other)

    def __repr__(self):
        return f"{self.lst_words}"
lst_text = []
for i in stich_v2:
    lst_text.append(StringText(i))

lst_text_sorted = sorted(lst_text, reverse=True)
print(lst_text_sorted)
lst_text_sorted = [' '.join(i.lst_words) for i in lst_text_sorted]
print(lst_text_sorted)