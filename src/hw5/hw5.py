def task_one(exist_str: str = "john marta james Morgan Adam Maria huang"):
    split_str = exist_str.split(' ')
    new_str = []

    for name in split_str:
        new_str.append(name.capitalize())

    return ' '.join(new_str)

def task_two(exist_list: list = ["John", "Marta", "James", "Amanda", "Marianna"]):
    new_list = 'Names'.center(15, '*') + '\n'
    for name in exist_list:
       new_list = new_list + (f'{name : >15}\n')
    return new_list

def task_three(first_str: str =  "name=Amanda=sssss&age=32&&salary=1500&currency=quro"):
    strip_str = first_str.strip()
    result = []
    replace_str = strip_str.replace('&&', '&')
    split_str = replace_str.split('&')
    for element in split_str:
        if '&' in element:
            element = element.replace('&', '')
        elif '=sssss' in element:
            element = element.replace('=sssss', '?sssss')
        element = element.replace('=', ': ')
        if '?' in element:
            element = element.replace('?', '=')
        result.append(element)
    result = '{' + ', '.join(result) + '}'
    return result

def task_four(camel_list: list = ["FirstItem", "FriendsList", "MyTuple"]):
    result = []
    for element in camel_list:
        new_list = []
        for letter in element:
            if letter.isupper() and element.index(letter) != 0:
                letter = letter.replace(letter, '_' + letter.lower())
            new_list.append(letter)
        new_str = ''.join(new_list)
        result.append(new_str.lower())
    return result

def task_five(text_str: str = """
Есть строка с именами разделенная пробелами "john marta james Morgan Adam Maria huang" преобразовать строку таким образом что бы каждое имя однозначно начиналось с большой буквы. 
Есть список друзей ["John", "Marta", "James", "Amanda", "Marianna"]. 
Выведите в консоль имена каждое с новой строки выровняв по правой стороне используя метод строки и форматирование через f string. 
Так же над именами первой строкой выведини заговловок Names где слово names должно быть посредине а остальное пространство заполнено скажем символом "*". 
Есть строка переданная в качестве квери параметров " name=Amanda=sssss&age=32&&salary=1500&currency=quro ". 
Преобразовать эту строку в словарь где ключем должно быть значение перед = а значение пары значение после равно {name: Amanda=sssss, age: 32, salary: 1500, currency: quro}. 
У вас есть список имен переменных в формате кэмел кейс ["FirstItem", "FriendsList", "MyTuple"] преобразовать его в список имен переменных для пайтона в формате снейк кейс ["first_item", "friends_list", "my_tuple"].
"""):
    new_str = text_str.strip().split('\n')
    result = []
    for sentence in new_str:
        # result += sentence.split('. ')
        result.append(sentence)
    for element in result:
        element = element + '.'
        if '..' in element:
            element = element.replace('..', '.')
    return result

if __name__ == '__main__':
    print(task_one())
    print(task_two())
    print(task_three())
    print(task_four())
    print(task_five())
