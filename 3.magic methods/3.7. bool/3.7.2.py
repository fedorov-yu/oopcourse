class MailBox:
    def __init__(self):
        self.inbox_list = list()

    def receive(self, *args):
        for mail in args:
            self.inbox_list.extend(mail)


class MailItem:
    def __init__(self, mail_from, title, content):
        self.mail_from = mail_from
        self.title = title
        self.content = content
        self.is_read = False

    def set_read(self, fl_read):
        self.is_read = fl_read

    def __bool__(self):
        return self.is_read

    def __repr__(self):
        return f"{self.mail_from} -- {self.is_read}"


lst_in = ['sc_lib@list.ru; От Балакирева; Успехов в IT!',
          'mail@list.ru; Выгодное предложение; Вам одобрен кредит.',
          'Python ООП; Балакирев С.М.; 2022',
          'mail123@list.ru; Розыгрыш; Вы выиграли 1 млн. руб. Переведите 30 тыс. руб., чтобы его получить.']

mail = MailBox()
mail.receive([MailItem(i.split(";")[0], i.split(";")[1], i.split(";")[2]) for i in lst_in])
mail.inbox_list[0].set_read(True)
# print(mail.inbox_list)
mail.inbox_list[-1].set_read(True)

inbox_list_filtered = list(filter(None, mail.inbox_list))
print(inbox_list_filtered)
