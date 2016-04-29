#!/usr/bin/python3


def ab(filename):

    try:
        f_input = open(filename, 'r')
        s = f_input.read()
        f_output = open('output.txt', 'w')
        result = str(int(s[0:1]) + int(s[2:]))
        f_output.write(result)
    except FileNotFoundError:
        print('{} - такого файла нет'.format(filename))
    except ValueError:
        print('Данные в файле некорректны')

    return 'Выполнено'

print(ab('input.txt'))
