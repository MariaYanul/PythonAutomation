from hidrohen import Hidrohen
from methane import Methane

class Carbone:

    def __init__(self) -> None:
        self.__number = 6
        self.__valence = 4
        self.__vuglec = 'C'

    def __str__(self) -> str:
        result = ""

        for key, value in self.__dict__.items():
            result += f"{key} => {value}\n"

        return result

    def __add__(self, other: Hidrohen):
        return Methane(self.__vuglec, other.voden)

    @property
    def vuglec(self):
        return self.__vuglec

