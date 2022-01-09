from cat_abc import Cat

class CatPurebred(Cat):
    def __init__(self, name: str, breed: str, age: int) -> None:
        super().__init__(name, breed, age)

    def eat(self):
        print('The purebred eats only special meal')

    def sleep(self):
        print('The purebred sleeps in its own bed')
