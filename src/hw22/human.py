class Human:

    def __init__(self, name: str, age: int, gender: str, weight: int) -> None:
        self.__name = name
        self.__age = age
        self.__gender = gender
        self.__weight = weight

    @property
    def name(self) -> str:
        return self.__name

    @property
    def age(self) -> int:
        return self.__age

    @property
    def gender(self) -> str:
        return self.__gender

    @property
    def weight(self) -> int:
        return self.__weight

    def __validate_gender(self, gender: str) -> str:
        if gender not in ['male', 'female']:
            raise Exception('Not supported gender...')
        else:
            return gender

    def grow_up(self) -> None:
        self.__age += 1

    def get_fat(self) -> None:
        self.__weight += 5

    def change_name(self, name: str) -> None:
        if name != self.__name:
            self.__name = name
        else:
            raise Exception('Provide name is same as current...')

    def change_gender(self, gender: str):
        self.__gender = self.__validate_gender(gender)
