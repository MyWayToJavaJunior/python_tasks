#!/usr/bin/python3
# -*- coding: utf-8 -*-

# список

# Заполните код преведенных ниже функций. Функция main() уже настроена
# для вызова функций с несколькими различными параметрами,
# и выводит 'OK' в случае, если вызов функции корректен.
# Начальный код каждой функции содержит 'return'
# и является просто заготовкой для вашего кода.


# A. Начало и конец совпадают
# Функция принимает в качестве аргумента список строк.
# Необходимо вернуть количество строк,
# длина которых составляет 2 символа и более, 
# а первый и последний символы этих строк совпадают.
# Примечание: в python нет оператора ++. Но += сработает.


def match_ends(words):
    count = 0
    for word in words:
        if len(word) >= 2 and word[0] == word[-1]:
            count += 1
    return count


# B. Начинающиеся с X в начале
# Функция принимает в качестве аргумента список строк.
# Необходимо вернуть отсортированный список строк, в котором:
# сначала идет группа строк, начинающихся на 'x', затем все остальные.
# Наример: из ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] получится
# ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
# Подсказка: это можно сделать при помощи склеивания 2х заранее отсортированных списков


def front_x(words):
    list_x = []
    for word in words:
        if word[0] == 'x':
            list_x.append(word)

    for i in range(len(words)):  # или так - for i in words: if word[0] != 'х'
        if words[i][0] != 'x':
            list_x.append(words[i])

    return list_x


def front_x2(words):
    x_words = []
    other_words = []

    for x in words:
        if x.starwith('x'):
            x_words.append(x)
        else:
            other_words.append(x)

    x_words.sort()
    other_words.sort()
    x_words.extend(other_words)

    return x_words


# C. Сортировка по последнему числу
# Дан спискок непустых списков.
# Нужно вернуть список, отсортированный по
# возрастанию последнего элемента каждого подсписка.
# Например: из [[1, 7], [1, 3], [3, 4, 5], [2, 2]] получится
# [[2, 2], [1, 3], [3, 4, 5], [1, 7]]
# Подсказка: используйте параметр key= функции сортировки,
# чтобы получить последний элемент подсписка.

def sort_last(lists):
    lists.sort(key=lambda i: i[-1])
    return lists


def sort_last1(lists):
    return sorted(list, key=lambda x: x[-1])

# Удаление соседей
# Дан список чисел.
# Нужно вернуть список, где все соседние элементы
# были бы сведены к одному элементу.
# Таким образом, из [1, 2, 2, 3, 4, 4] получится [1, 2, 3, 4].


def remove_adjacent(nums):
    if nums:
        new_list = []
        new_list.append(nums.pop(0))
        count = 0
        while count < len(nums):
            if nums[count] != new_list[count]:
                new_list.append(nums[count])
                count += 1
            elif nums[count] == new_list[count]:
                nums.pop(count)
    else:
        new_list = []

    return new_list


def remove_adjacent(nums):
    prev = None
    res = []

    for x in nums:
        if x != prev:
            res.append(x)
        prev = x

    return res


# Простая функция test() используется в main() для вывода
# сравнения того, что возвращает с функция с тем, что она должна возвращать.

def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('%s Получено: %s | Ожидалось: %s' % (prefix, repr(got), repr(expected)))


# Вызывает фунции выше с тестовыми параметрами.
def main():
    print('Начало и конец совпадают')
    test(match_ends(['aba', 'xyz', 'aa', 'x', 'bbb']), 3)
    test(match_ends(['', 'x', 'xy', 'xyx', 'xx']), 2)
    test(match_ends(['aaa', 'be', 'abc', 'hello']), 1)

    print()
    print('Начинающиеся с X в начале')
    test(front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa']),
       ['xaa', 'xzz', 'axx', 'bbb', 'ccc'])
    test(front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa']),
       ['xaa', 'xcc', 'aaa', 'bbb', 'ccc'])
    test(front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark']),
       ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'])

    print()
    print('Сортировка по последнему числу')
    test(sort_last([[1, 3], [3, 2], [2, 1]]),
       [[2, 1], [3, 2], [1, 3]])
    test(sort_last([[2, 3], [1, 2], [3, 1]]),
       [[3, 1], [1, 2], [2, 3]])
    test(sort_last([[1, 7], [1, 6], [3, 4, 5], [2, 2]]),
       [[2, 2], [3, 4, 5], [1, 6], [1, 7]])

    print()
    print('Удаление соседей')
    test(remove_adjacent([1, 2, 2, 3]), [1, 2, 3])
    test(remove_adjacent([2, 2, 3, 3, 3, 3]), [2, 3])
    test(remove_adjacent([4, 5, 5, 4, 4]), [4, 5, 4])
    test(remove_adjacent([]), [])


if __name__ == '__main__':
    main()
