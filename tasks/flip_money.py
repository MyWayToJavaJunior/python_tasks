#!/usr/bin/python3

from re import findall

s = '5\n0\n0\n1\n1\n1\n0'


def flip_money(string):

    num_list = [int(i) for i in findall(r'[^\s]', string)][1:]
    if num_list.count(1) - num_list.count(0) > 0:
        return num_list.count(0)
    elif num_list.count(1) - num_list.count(0) < 0:
        return num_list.count(1)
    else:
        return 'Без разницы'


print(flip_money(s))
