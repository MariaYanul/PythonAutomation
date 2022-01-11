class Methane:

    def __init__(self, vuglec: str, voden: str) -> None:
        self.__vuglec = vuglec
        self.__voden = voden

    def __str__(self) -> str:
        result = ""

        for key, value in self.__dict__.items():
            result += f"{key} => {value}\n"

        return result
