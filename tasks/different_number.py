#!/usr/bin/python3

"""
Подсчитывает, сколько различных чисел содержится в данном списке
"""


def dif_number(string):
    a = set([int(x) for x in string.split()])

    print(len(a))


print(dif_number('2 5 1 3 1 1 1 2 23'))
