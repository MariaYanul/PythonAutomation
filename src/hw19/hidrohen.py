class Hidrohen:

    def __init__(self) -> None:
        self.__number = 1
        self.__valence = 1
        self.__voden = 'H'

    def __str__(self) -> str:
        result = ""

        for key, value in self.__dict__.items():
            result += f"{key} => {value}\n"

        return result

    @property
    def voden(self):
        return self.__voden + '4'


