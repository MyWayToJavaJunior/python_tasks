"""
Уравнение для пятиклассников представляет собой строку длиной 5 символов. Второй символ строки является либо знаком
'+' (плюс) либо '-' (минус), четвёртый символ — знак '=' (равно). Из первого, третьего и пятого символов ровно два
являются цифрами из диапазона от 0 до 9, и один — буквой x, обозначающей неизвестное.

Требуется написать программу, которая позволит решить данное уравнение относительно x
"""

from re import compile, match, search


def easy_eqution(equ):

    if equ.count('x') > 1:
        return 'Некорректный ввод, у вас болле двух неизвестных'

    r = compile(r'(\-*[(0-9)|x])\s*([+-])\s*([(0-9)|x])\s*=\s*(\-*[(0-9)|x])\s*')
    s = r.search(equ)

    opt = s.group(2)

    if opt == '+':
        if s.group(1) == 'x' or s.group(1) == '-x':
            return '{} = {}'.format(s.group(1), int(s.group(4)) - int(s.group(3)))
        elif s.group(3) == 'x':
            return '{} = {}'.format(s.group(3), int(s.group(4)) - int(s.group(1)))
        else:
            return '{} = {}'.format(s.group(4), int(s.group(1)) + int(s.group(3)))
    elif opt == '-':
        if s.group(1) == 'x' or s.group(1) == '-x':
            return '{} = {}'.format(s.group(1), int(s.group(4)) + int(s.group(3)))
        elif s.group(3) == 'x':
            return '{} = {}'.format(s.group(3), int(s.group(4)) - int(s.group(1)))
        else:
            return '{} = {}'.format(s.group(4), int(s.group(1)) - int(s.group(3)))


print(easy_eqution('-x+5=7'), '-x = 2', sep=' ::: ')
print(easy_eqution('x+5=7'), 'x = 2', sep=' ::: ')
print(easy_eqution('-5+x=7'), 'x = 12', sep=' ::: ')
print(easy_eqution('2+3=x'), 'x = 5', sep=' ::: ')
print('--------------------')
print(easy_eqution('x-5=7'), 'x = 12', sep=' ::: ')
print(easy_eqution('-x-5=7'), '-x = 12', sep=' ::: ')
print(easy_eqution('5-x=7'), 'x = 2', sep=' ::: ')
print(easy_eqution('2-3=x'), 'x = -1', sep=' ::: ')




