#!/usr/bin/python3

"""
Вам необходимо проверить домашнюю работу Васи Пупкина, в которой он написал равенство. Например, запись вида «2+3=5»
является правильной, а «23*7=421» неверная, но корректная. Корректной записью выражения будем называть
последовательность: число, операция («+», «-», «*», «/»), число, знак равенства, число. Т.е. если в записи не
хватает цифр или же встречается неизвестный символ. Например, записи «2*=3», «173» и «2+2=a» некорректны.
"""

import re


def check_equal(string):

    op = ['*', '/', '+', '-']

    res = re.compile(r'\s*(\d+)\s*([+*\/-])\s*(\d+)\s*=\s*(\d+)\s*')  # не понимаю почему по группам не разбежались

    if res.match(string):

        equality = res.findall(string)
        one = int(equality[0][0])  # костыль, после вернуться и исправить
        two = int(equality[0][2])  # разбить по группам
        res = int(equality[0][3])
        i = op.index(equality[0][1])

        if op[i] == '*':
            return 'YES' if one * two == res else 'NO'
        elif op[i] == '/':
            return 'YES' if one / two == res else 'NO'
        if op[i] == '+':
            return 'YES' if one + two == res else 'NO'
        if op[i] == '-':
            return 'YES' if one * two == res else 'NO'
    else:
        return 'ERROR'

print(check_equal('23+7=421'))
print(check_equal('	2+3=5'))
print(check_equal('3*7=20'))
print(check_equal('two plus three is five'))
