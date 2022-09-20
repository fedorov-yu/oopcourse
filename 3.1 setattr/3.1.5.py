from typing import List


class SmartPhone:

    def __init__(self, model, ):
        self.model = model
        self.apps: List[AppVK, AppYouTube, AppPhone] = []

    def add_app(self, app):
        if len(tuple(filter(lambda x: type(x) == type(app), self.apps))) == 0:
            self.apps.append(app)

    def remove_app(self, app):
        if app in self.apps:
            self.apps.remove(app)


class AppVK:

    def __init__(self, ):
        self.name = "ВКонтакте"


class AppYouTube:

    def __init__(self, memory_max):
        self.name = "YouTube"
        self.memory_max = memory_max


class AppPhone:

    def __init__(self, phone_list: dict = {}):
        self.name = "Phone"
        self.phone_list = phone_list


sm = SmartPhone("Honor 1.0")
sm.add_app(AppVK())
sm.add_app(AppVK())  # второй раз добавляться не должно
sm.add_app(AppYouTube(2048))
sm.add_app(AppPhone({"Балакирев": 1234567890, "Сергей": 98450647365, "Работа": 112}))
sm.add_app(AppPhone({"Балакирев": 1234567890, "Сергей": 98450647365, "Работа": 112}))
for a in sm.apps:
    print(a.name)
