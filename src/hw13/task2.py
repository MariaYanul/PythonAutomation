ls = [1, 2, 3, 4, 5]

def main():
    for i in range(len(ls), 15):
        ls.append(i + 1)
        if len(ls) >= 10:
            raise Exception('List can contain only 10 elements')

try:
   main()
except Exception as err:
    print(err)
finally:
    print('ok')
