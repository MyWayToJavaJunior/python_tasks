#!/usr/bin/python3
# -*- coding: utf-8 -*-

import time

"""
Напишите на Python две функции для поиска
минимального значения в списке.
Первая из них должна сравнивать каждое число
со всеми другими значениями в списке.
O(n^2). Вторая функция должна быть
линейной с O(n)
"""

import random


def get_list(n):

    r = random.sample(range(1, 101), n)

    return r


def time_work(func):

    def decorated(*args, **kwargs):
    
        start = time.time()

        result = func(*args, **kwargs)

        print('Время - {} ; результат - {}'.format(time.time() - start, result))
        return result
        
    return decorated


# O(n)
@time_work
def min_list1(alist):

    minim = float('Inf')

    for i in alist:
        if i < minim:
            minim = i

    return minim


# O(n^2)
@time_work
def min_list2(alist):

    minim = alist[0]

    for i in alist:
        issmallest = True
        for j in alist:
            if i > j:
                issmallest = False
        if issmallest:
            minim = i
    return minim
        

l = get_list(100)

min_list1(l)
min_list2(l)
