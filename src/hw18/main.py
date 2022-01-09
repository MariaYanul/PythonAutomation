from cat_abc import Cat
from yard_cat import CatYard
from purebred_cat import CatPurebred

if __name__ == '__main__':
    cat_1 = CatYard('Barsik', 'Courtyard cat', 3)
    cat_2 = CatPurebred('Iris', 'Purebred cat', 6)

    cat_1.eat()
    cat_2.eat()

    cat_1.sleep()
    cat_2.sleep()
