from abc import ABC, abstractmethod


class Model(ABC):
    @abstractmethod
    def get_pk(self):
        pass

    @staticmethod
    def get_info():
        return "Базовый класс Model"


class ModelForm(Model):
    ID = 0

    def __init__(self, login, password):
        self._login = login
        self._password = password
        self._id = self.ID
        ModelForm.ID += 1

    def get_pk(self):
        return self._id
