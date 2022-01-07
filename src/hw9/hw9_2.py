from typing import Union
from math import sqrt

def arithmetic(side_square: float):
    ls = []
    perimeter = side_square * 4
    ls.append(perimeter)
    square_area = side_square ** 2
    ls.append(square_area)
    diagonal_square = sqrt(2) * side_square
    ls.append(diagonal_square)
    res = tuple(ls)
    return res

if __name__ == '__main__':
    print(arithmetic(2))
    print(arithmetic(3))
    print(arithmetic(0))
