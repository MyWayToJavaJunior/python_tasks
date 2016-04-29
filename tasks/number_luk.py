#!/usr/bin/python3
"""
Числа Люка (как и числа Фибоначчи) задаются рекурентной формулой
Ln = Ln-1 + Ln-2, но с начальными значениями L0 = 2 и L1 = 1

2, 1, 3, 4, 7, 11, 18, 29, 47, 76, 123, 199, 322...

Найти 43-е число Люка, если 2 считать нулевым числом ряда
"""

def number_luk(max_number):

    a = 2
    b = 1
    result = []

    while a < max_number:

        result.append(a)
        a, b = b, b + a
        
        if len(result) == 43:
            return result.pop()


print(number_luk(600000000))
