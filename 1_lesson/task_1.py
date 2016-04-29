# -*- coding: utf-8 -*-

# 1
# реализовать реверс строки четырьмя разными способами


# способ 1-ый
def l_reverse(str):
    l = list(str)
    l.reverse()
    return ''.join(l)


# способ 5
def reversed(str):
    return " ".join(reversed(list(str)))


# способ 6
def list_manual_reverse(str):
    result = []
    for letter in str:
        result.insert(0,letter)
    return " ".join(result)


# способ 2
def reverse(s):
    return " ".join(s.split(" ")[::-1])


# способ 3
def str_reverse(arg):
    arr = list(arg)
    output = ''
    for i in range(0, len(arr) + 1):
        output += arr.pop()
    return output


# способ 4
def str_reversed(arg):
    output = ''
    for i in range(1,len(arg) + 1):
        output += arg[-1]
    return output


# 2
# подсчет гласных букв из строки латинского алфавита
# гласные - 'a', 'e', 'i', 'o', 'u'
def gla_word(str):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for letter in str:
        if letter.lower() in vowels:
            count += 1
    return count


# 3
# подстчет вхождений подстроки.
# Реализовать подсчеты количества вхождений подстроки "wow" в строке
def find_str(str):
    wows = 0
    for i in range(1, len(str) - 1):
        if str[i-1:i+2] == 'wow':
            wows += 1
    return wows

# 4
# упорядоченная подстрока.
# Построить функционал который будет находить в строке подстроку максимальной длины,
# в которой буквы упорядочены в алфавитном порядке.'a b c d e f'


def alpha_bet(s):
    final = ''
    output = ''
    prev = ''
    for i in s:
        if i >= prev:
            output += i
            if len(final) < len(output):
                final = output
        else:
            output = i
        prev = i
    return final

# 5
# УСЛОВИЕ:функция, которая принимает объект и выводит
# строку с наименованием типа этого объекта


def typer(arg):
    return typer(arg).__name__  # str(type(arg))[8:-2]

# 6
# Написать фрагмент python кода, который будет анализировать две переменные (А и В),
# которые могут быть типа "str" или "int".
# В зависимости от значения переменных код должен выводить на печать ОДНО из следующих сообщений:
# - "получена строка" - если хотя бы одна из переменных является строкой;
# - "больше" - если А больше В;
# - "равны" - если значения переменных равны;
# - "меньше" - если А меньше В.


def analize(a, b):
    if type(a) == str or type(b) == str:
        print('Получена строка')
    elif type(a) == int and type(b) == int:
        if a == b:
            print('равны')
        elif a > b:
            print('больше')
        elif a < b:
            print('меньше')
    return

# 7
# уникальный набор


def uniq_ord(l):
    result = []
    for item in l:
        if not item in result:
            result.append(item)
    return result


def unique_disordered(L):
    return list(set(L))


def uniq_disord(l):
    return sorted(list(set(l)))

# 8
# каждый третий , на входе кортеж


def every_three(t):
    result = []
    for i in range(2, len(t)+1, 3):
        result.append(t[i])
    return tuple(result)

t = (1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 'a', 'b', 'c')


# 9
def xyz(x, y, z):
    return min(max(x, y), z)


# 10
def vowels_console():
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    str_cons = raw_input()
    for letter in str_cons:
        if letter.lower() in vowels:
            count += 1
    print(count)
    return count


# vowels_console()