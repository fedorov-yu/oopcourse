class Aircraft:
    def __init__(self, model: str, mass: int, speed: int, top: int):
        self.__checker(model, mass, speed, top)
        self._model = model
        self._mass = mass
        self._speed = speed
        self._top = top

    @staticmethod
    def __checker(model, mass, speed, top):
        if type(model) != str or not (type(mass) in (int, float) and mass >= 0) or not (
                type(speed) in (int, float) and speed >= 0) or not (type(top) in (int, float) and top >= 0):
            raise TypeError('неверный тип аргумента')


class PassengerAircraft(Aircraft):
    def __init__(self, model, mass, speed, top, chairs):
        super().__init__(model, mass, speed, top)
        if not type(chairs) == int:
            raise TypeError('неверный тип аргумента')
        self._chairs = chairs


class WarPlane(Aircraft):
    def __init__(self, model, mass, speed, top, weapons):
        super().__init__(model, mass, speed, top)
        if not type(weapons) == dict:
            raise TypeError('неверный тип аргумента')
        self._weapons = weapons


planes = [PassengerAircraft('МС-21', 1250, 8000, 12000.5, 140),
          PassengerAircraft('SuperJet', 1145, 8640, 11034, 80),
          WarPlane('Миг-35', 7034, 25000, 2000, {"ракета": 4, "бомба": 10}),
          WarPlane('Су-35', 7034, 34000, 2400, {"ракета": 4, "бомба": 7})]