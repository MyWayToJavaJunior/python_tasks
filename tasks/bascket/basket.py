#!/usr/bin/python3

import re


def score_match(filename):
    try:
        s = open(filename, 'r')
        num_list = re.findall(r'(\d{2})+', s.read())

        a = 0  # a = int(num_list[0])
        b = 0  # b = int(num_list[1])

        for i in range(0, len(num_list)):
            if i % 2 == 0 or i == 0:
                a += int(num_list[i])

            if not(i % 2 == 0) or i == 1:
                b += int(num_list[i])

        print('Результат - {} : {}'.format(a, b))

    except FileNotFoundError:
        print('Файл не найден')

    except ValueError:
        print('Данные в файле некорректны')

    return 'Выполнено'


score_match('input.txt')
