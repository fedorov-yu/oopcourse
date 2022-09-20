from random import randint, choice  # функция для генерации целых случайных значений в диапазоне [a; b]


# здесь объявляйте класс RandomPassword
class RandomPassword:

    def __init__(self, psw_chars, min_length, max_length):
        self.__chars = psw_chars
        self.__min_length = min_length
        self.__max_length = max_length

    def __call__(self, *args, **kwargs):
        psww = ''
        for i in range(randint(self.__min_length, self.__max_length)):
            psww += choice(self.__chars)

        return psww


min_length = 5
max_length = 20
psw_chars = "qwertyuiopasdfghjklzxcvbnm0123456789!@#$%&*"
rnd = RandomPassword(psw_chars, min_length, max_length)
lst_pass = [rnd() for _ in range(3)]
print(lst_pass)
