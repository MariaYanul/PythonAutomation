def escape_sequences(escape_element, name):
    if 11 < len(name) < 20:
        tab_number = 3
    elif len(name) < 10 or len(name) == 11:
        tab_number = 4
    else:
        tab_number = 1
    return f'|\t{escape_element}\t|\t{name}' + '\t' * tab_number + '|'

if __name__ == '__main__':
    print('Escape sequences table:')
    print('-' * 37)
    print(escape_sequences(r'\a', 'Bell (alert)'))
    print(escape_sequences(r'\b', 'Backspace'))
    print(escape_sequences(r'\n', 'New line'))
    print(escape_sequences(r'\t', 'Horizontal tab'))
    print(escape_sequences(r'\\', 'Backslash \\'))
    print(escape_sequences(r'\"', 'Double quotation mark \"'))
    print(escape_sequences(r'\'', 'Single quotation mark \''))
    print('-' * 37)
