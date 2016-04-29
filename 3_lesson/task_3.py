# 1
# Посчитать количество гласных в каждом слове текста.
# Вывести максимальное количество гласных в одном слове.
# Гласные: A, E, I, O, U, Y

TEXT = '''Proin eget tortor risus. Cras ultricies ligula sed magna dictum porta.
Proin eget tortor risus. Curabitur non nulla sit amet nisl tempus convallis quis ac lectus.
Donec rutrum congue leo eget malesuada.'''

VOWELS = 'AEIOUY'


def number_vowels(text, vowels):
    words_list = text.split()
    count_result = []

    for words in words_list:
        count_vowels = 0

        for vow in words:
            if vow.upper() in vowels:
                count_vowels += 1
        count_result.append(count_vowels)

    return max(count_result)


# print(number_vowels(TEXT, VOWELS))


# 2
# Найти слово максимальной длины в тексте.
# Вывести это слово. Если таких слов несколько - вывести все.


def max_length(text):
    words = text.split()
    clean_words = [word.rstrip('.,:') for word in words]
    max_len = max(len(word) for word in clean_words)

    return [word for word in clean_words if len(word) == max_len]

# print(max_length(TEXT))


# 3
# УСЛОВИЕ:
# Изменить в тексте порядок следования:
# - букв в словах;
# - слов в предложениях;
# - предложений в тексте.
# Вывести модифицированный текст.


TEXT_R = '''Lorem, ipsum dolor sit amet, consectetur adipiscing elit. Nulla quis lorem ut libero malesuada feugiat. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec rutrum congue leo eget malesuada. Cras ultricies ligula sed magna dictum porta.'''


# TEXT_R = "Lorem ipsum dolor sit amet, consectetur adipiscing elit." + \
#     "Nulla quis lorem ut libero malesuada feugiat. Lorem ipsum dolor sit " + \
#     "amet, consectetur adipiscing elit." + \
#     "Donec rutrum congue leo eget malesuada." + \
#     "Cras ultricies ligula sed magna dictum porta."

def all_reverse(text):
    words = text.split()
    reverse_text = []
    for word in words:
        reverse_text.append(word[::-1])
    reverse_text.reverse()
    return ' '.join(reverse_text)

# print(all_reverse(TEXT_R))


# 4
# УСЛОВИЕ:
# Произвести импортирование модулей стандартной библиотеки Python: "os" и "sys".
# Вывести справку по всем функциям каждого модуля.


import os # from os import *
import sys # from sys import *

# print(dir(sys))
# print(dir(os))


def show_guts(module):
    """Prints module objects docstrings"""

    def sep_line(sep="=", n=70):
        print(sep * n)

    sep_line()
    print("DOCSTRINGS OF '%s' MODULE\n\n" % module.__name__)
    for obj_name in dir(module):
        if not obj_name.startswith("_"):
            print(obj_name)
            sep_line(".")
            print(eval("{module_name}.{object_name}.__doc__".format(**{"module_name": module.__name__, "object_name": obj_name})))
            sep_line()


# print(show_guts(sys))

# 5
# УСЛОВИЕ:
# Принимать любое натуральное число.
# Выдавать сумму цифр, из которых число состоит.
# Не использовать оператор "+" и встроенную функцию sum().


def pseudosum(num):
    base_list = [0]
    base_list.extend(list(str(num)))
    return abs(reduce(lambda x, y: x - int(y), base_list))


# 6
# УСЛОВИЕ:
# Вывести на печать 10000 первых натуральных простых чисел.
# Напомню, что это те, которые делятся без остатка на себя и 1, начиная с числа 2.


def natural_number(x):
    return [number for number in range(2, x + 1) if (number % 2 != 0) and (number % 3 != 0)]


# print(natural_number(10000))


# 7
# Выполнить задание 3 с сохранением позиций:
# - знаков препинания ("word," >> "drow,");
# - Заглавных букв в начале предложения ("Word ..." >> "Drow ...").


def reverse_all(text):
    words = text.split()
    reverse_text = []
    for word in words:
        if word[0] == word[0].upper():
            reverse_text.append(word[::-1].capitalize())
        else:
            reverse_text.append(word[::-1])
    reverse_text.reverse()
    return ' '.join(reverse_text)

# самая первое слово не меняется
# print(reverse_all(TEXT_R))


# 8
# УСЛОВИЕ:
# Посчитать в тексте количество букв "a" при условии что она окружена согласными
# ("car") и она не является первой или последней буквой слова.
# Согласные: все, кроме A, E, I, O, U, Y

text_a = '''Cras ultricies ligula sed magna dictum porta. Vivamus magna justo, lacinia eget consectetur sed, convallis at tellus. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Donec velit neque, auctor sit amet aliquam vel, ullamcorper sit amet ligula. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur aliquet quam id dui posuere blandit. Quisque velit nisi, pretium ut lacinia in, elementum id enim. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed porttitor lectus nibh.'''

import string


def count_a(text):
    vowels = "aeiouy"
    valid_letters = string.ascii_letters
    counter = 0
    for i, letter in enumerate(text[1:-1], start=1):
        if letter.lower() == vowels[0]:
            prev_letter = text[i-1].lower()
            next_letter = text[i+1].lower()
            if (prev_letter not in vowels and prev_letter in valid_letters
                and next_letter not in vowels and next_letter in valid_letters):
                counter += 1

    return counter

# print(count_a(text_a))


def hello(name, surname='', title='Mr.'):
    '''
    Hello!
    '''
    if surname:
        surname = ' ' + surname.strip()
    print('Hello {0} {1}{2}'.format(title, name, surname))


# hello('john')
# hello('John', 'Galt', 'Sir')
# hello('John', title='Sir')
# hello('John', title='Sir', surname='Galt')
# hello(title='Sir', surname='Galt', name='john')
# print(hello.__doc__)