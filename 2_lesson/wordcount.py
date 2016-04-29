#!/usr/bin/python3
# -+- coding: utf-8 -+-

# Упражнение "Количество слов"
# Функция main() ниже уже определена и заполнена. Она вызывает функции
# print_words() и print_top(), которые вам нужно заполнить.
#
# 1. Если при вызове файла задан флаг --count, вызывается функция
# print_words(filename), которая подсчитывает, как часто каждое слово встречается
# в тексте и выводит:
# слово1 количество1
# слово2 количество2
# ...
#
# Выводимый список отсортируйте в алфавитном порядке. Храните все слова
# в нижнем регистре, т.о. слова "Слон" и "слон" будут обрабатываться как одно
# слово.
#
# 2. Если задан флаг --topcount, вызывается функция print_top(filename),
# которая аналогична функции print_words(), но выводит только топ-20 наиболее
# часто встречающихся слов, таким образом первым будет самое часто встречающееся
# слово, за ним следующее по частоте и т.д.
#
# Используйте str.split() (без аргументов), чтобы разбить текст на слова.
#
# Отсекайте знаки припинания при помощи str.strip() с знаками припинания
# в качестве аргумента.
#
# Совет: не пишите всю программу сразу. Доведите ее до какого-то промежуточного
# состояния и выведите вашу текущую структуру данных. Когда все будет работать
# как надо, перейдите к следующему этапу.
#
# Дополнительно: определите вспомогательную функцию, чтобы избежать дублирования
# кода внутри print_words() и print_top().

# Определите и заполните функции print_words(filename) и print_top(filename).
# Вы также можете написать вспомогательную функцию, которая читает файл,
# строит по нему словарь слово/количество и возвращает этот словарь.
# Затем print_words() и print_top() смогут просто вызывать эту вспомогательную функцию.

# Это базовый код для разбора аргументов коммандной строки.
# Он вызывает print_words() и print_top(), которые необходимо определить.


import sys
import string


def get_word_dict(filename):

    f = open(filename, 'r', encoding='utf-8')
    word_list = f.read().split()

    res = {}

    chars_to_remove = string.punctuation + string.whitespace
    for w in word_list:
        w = w.lower().strip(chars_to_remove)
        # if w in res:
        #     res[w] += 1
        # else:
        #     res[w] = 1
        if w:
            res[w] = res.get(w, 0) + 1

    return res


def print_words(filename):
    word_dict = get_word_dict(filename)

    for k, v in sorted(word_dict.items(), key=lambda x: x[0]):
        print('{:20} {:5}'.format(k, v))


def print_top(filename):
    word_dict = get_word_dict(filename)

    for k, v in sorted(word_dict.items(), key=lambda x: x[1], reverse=True)[:20]:
        print('{:20} {:5}'.format(k, v))


def main():
    if len(sys.argv) != 3:
        print('usage: python wordcount.py {--count | --topcount} file')
        sys.exit(1)

    option = sys.argv[1]
    filename = sys.argv[2]
    if option == '--count':
        print_words(filename)
    elif option == '--topcount':
        print_top(filename)
    else:
        print('unknown option: ' + option)
    sys.exit(1)

if __name__ == '__main__':
    main()
