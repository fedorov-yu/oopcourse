from abc import ABC, abstractmethod


class CountryInterface(ABC):

    @property
    @abstractmethod
    def name(self):
        pass

    @name.setter
    @abstractmethod
    def name(self, value):
        pass

    @property
    @abstractmethod
    def population(self):
        pass

    @population.setter
    @abstractmethod
    def population(self, value):
        pass

    @property
    @abstractmethod
    def square(self):
        pass

    @square.setter
    @abstractmethod
    def square(self, value):
        pass

    @abstractmethod
    def get_info(self):
        raise NotImplementedError()


class Country(CountryInterface):
    def __init__(self, name: str, population: int, square: int):
        self._name = name
        self._population = population
        self._square = square

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def population(self):
        return self._population

    @population.setter
    def population(self, value):
        self._population = value

    @property
    def square(self):
        return self._square

    @square.setter
    def square(self, value):
        self._square = value

    def get_info(self):
        return f"{self._name}: {self._square}, {self._population}"


country = Country("Россия", 140000000, 324005489.55)
name = country.name
pop = country.population
country.population = 150000000
country.square = 354005483.0
