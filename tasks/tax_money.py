#!/usr/bin/python3

"""
Ежегодно с суммы имеющихся наличных, должны отдать 7%, независимо от того, заработали они в этом году или они сохранились с прошлого года. Округляется в меньшую сторону(7% - 1.9 = 1)

заработок в год = 40
первоначальное состояние = 777
сколько денег будет через 10 лет?
"""

import math

def tax_money(salary_year, bank, percent, count_year):

    percent = 1 - percent / 100

    for i in range(0, count_year):
        bank = math.floor((bank + salary_year) * percent)
    return bank

print(tax_money(40, 777, 7, 2))
