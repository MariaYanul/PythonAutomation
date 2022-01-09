from typing import Union

def arithmetic(first_num: float, second_num: float, operation: str)  -> Union[float, str]:

    if operation == '+':
        res = first_num + second_num
    elif operation == '-':
        res = first_num - second_num
    elif operation == '*':
        res = first_num * second_num
    elif operation == '/':
        res = first_num / second_num
    else:
        res = f"Not known operation: {operation}"
    return res

if __name__ == '__main__':
    print(arithmetic(3, 2, '+'))
    print(arithmetic(100, 57, '-'))
    print(arithmetic(4, 4, '*'))
    print(arithmetic(27, 3, '/'))
    print(arithmetic(2, 2, '**'))
