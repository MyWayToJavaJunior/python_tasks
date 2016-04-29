#!/usr/bin/python3

"""
оценка времени работы

программа на входе получила n = 1000 чисел. Оценить время этой же программы, если на входе будет 5000 чисел

"""

import time


def f(n):
    s = 0

    start = time.time()
    for i in range(n):
        s += i
    finish = time.time() - start
    print(n, finish, sep=' = ')

    return finish

print(f(5000) - f(1000))
