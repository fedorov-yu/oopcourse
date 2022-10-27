class Food:
    def __init__(self, name: str, weight: int, calories: int):
        self._name = name
        self._weight = weight
        self._calories = calories


class BreadFood(Food):
    def __init__(self, name: str, weight: int, calories: int, white: bool):
        super().__init__(name, weight, calories)
        self._white = white


class SoupFood(Food):
    def __init__(self, name: str, weight: int, calories: int, dietary: bool):
        super().__init__(name, weight, calories)
        self._dietary = dietary


class FishFood(Food):
    def __init__(self, name: str, weight: int, calories: int, fish: str):
        super().__init__(name, weight, calories)
        self._fish = fish
