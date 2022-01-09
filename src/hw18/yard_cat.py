from cat_abc import Cat

class CatYard(Cat):
    def __init__(self, name: str, breed: str, age: int) -> None:
        super().__init__(name, breed, age)

    def eat(self):
        print('The yard cat eats everything')

    def sleep(self):
        print('The yard sleeps everywhere')
