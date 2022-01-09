from abc import ABC, abstractmethod

class Cat(ABC):
    def __init__(self, name: str, breed: str, age: int) -> None:
        self._name = name
        self._breed = breed
        self._age = age

    @abstractmethod
    def eat(self):
        ...

    @abstractmethod
    def sleep(self):
        ...
