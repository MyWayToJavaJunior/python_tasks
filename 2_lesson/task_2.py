# 1
# принимает список или кортеж чисел
# возвращает набор того же типа
# со значениями квадратов этих чисел


def squaring(l):
    result = [x * x for x in l]
    if type(l) is tuple:
        result = tuple(result)
    return result


def squares_2(l):
    type_name = type(l)
    return type_name([item ** 2 for item in l])


def squares_3(l):
    return type(l)(map(lambda x: x**2, l))


# print(squaring((1, 2, 3, 4, 5)))


# 2
# Симметрия
# Фрагмент кода, который принимает строку и определяет симметрична ли строка.
# Возвращает True или False


def palindrome(d):
    return d == d[::-1]


def symmetry_2(string):
    while len(string) > 1:
        if string[0] != string[-1]:
            return False
        string = string[1:-1]
    return True

# print(palindrome('abba'))
# print(palindrome('arbat'))


# 3
# Фрагмент кода, который принимает список любых чисел и возвращает словарь вида:
# {число: boolean}, где: boolean - True или False в зависимости делится ли число на 3
# без остатка.


def list_hash(l):
    d = {}
    result_keys = [x % 3 == 0 for x in l]
    for i in range(len(l)):
        d[l[i]] = result_keys[i]
    return d

# print(list_hash([3, 7, 12, 43, 30, 123]))


def triples_2(l):
    return dict((item, (item % 3 == 0)) for item in l)


# 4
# Фрагмент кода, который принимает список любых чисел и фильтрует его по четным (удаляет нечетные),
# если количество элементов в списке является четным и наоборот
# (удаляет четные, если элементов изначально нечетное количество).


def even(l):
    if len(l) % 2 == 0:
        return list(filter(lambda x: x % 2 == 0, l))
        # result = [x % 2 == 0 for x in l]
    else:
        return list(filter(lambda x: not x % 2 == 0, l))
        # result = [not x % 2 == 0 for x in l]

# print(even([3, 7, 12]))
# print(even([3, 7, 12, 7]))


def evenodd_3(l):
    return [item for item in l if len(l) % 2 == item % 2]

# print(evenodd_3([3, 7, 12]))


# 5
# Фрагмент кода, который принимает список любых чисел и модифицирует его следующим образом:
# - в начале списка идут нечетные числа в порядке возрастания,
# - далее идут четные числа в порядке убывания.


def sep(l):
    no_even_sort = sorted(list(filter(lambda x: not x % 2 == 0, l)))
    even_reverse_sort = sorted(list(filter(lambda x: x % 2 == 0, l)), reverse=True)

    return no_even_sort + even_reverse_sort

# print(sep([1, 4, 8, 6, 3, 7, 1]))


def separ_1(l):
    evens = []
    for item in l:
        if item % 2 == 0:
            evens.append(item)
            l.remove(item)
    l.sort()
    evens.sort(reverse=True)
    l.extend(evens)
    return l


def separ_2(l):
    evens = []
    odds = []
    for item in sorted(l):
        evens.insert(0, item) if item % 2 == 0 else odds.append(item)
    return odds + evens


def separ_3(l):
    result = []
    for item in sorted(l, reverse=True):
        result.insert(0, item) if item % 2 == 1 else result.append(item)
    return result


# 6
# Фрагмент кода, который принимает словарь со значениями элементов разных типов,
# а возвращает словарь вида {имя_типа : количество_элементов_этого_типа.


def classifier(d):
    result = []
    result_d = {}
    for values in iter(d.values()):
        result.append(type(values).__name__)

    for i in range(len(result)):
        if not i in d:
            result_d[result[i]] = result.count(result[i])

    return result_d

# print(classifier({'a': 1, 3: [1,5], 'e': 'abc', '6': [], 't': 3, 123: {}, 4: []}))


def classified_1(d):
    result = {}
    for value in d.values():
        type_name = type(value).__name__
        if type_name in result:
            result[type_name] += 1
        else:
            result[type_name] = 1
    return result


def classified_2(d):
    result = {}
    for value in d.values():
        type_name = type(value).__name__
        result[type_name] = result.setdefault(type_name, 0) + 1
    return result

# 7
# Выполнить задание 5 ("Сепаратор") с дополнительным условием:
# чтобы входящий список и список возвращаемый были одним и тем же объектом, т.е.
# должна произойти модификация списка, а не пересборка нового.


def separ_inplace_1(l):
    m = l
    evens = []
    for item in l:
        if item % 2 == 0:
            evens.append(item)
            l.remove(item)
    l.sort()
    evens.sort(reverse=True)
    l.extend(evens)
    print(m is l)
    return l


# 8
# Фрагмент кода, который принимает кортеж любых чисел и модифицирует его
# в кортеж кортежей по два элемента (парами).


def many_tuple(t):
    result = list(t)
    tup = []
    for i in range(0, len(result), 2):
        tup.append(tuple(result[i:i+2]))
    return tuple(tup)

# print(many_tuple((1, 4, 8, 6, 3, 7, 1)))


def double_tuple_2(t):
    return tuple([t[i:i+2] for i, item in enumerate(t) if i % 2 == 0])


# 9
# Фрагмент кода, который принимает список списков, и делает список "плоским" -
# разворачивая элементы внутренних списков во вмещающий список.


def list_merge(l):
    all_l = []
    for i in l:
      all_l.extend(i)
    return all_l

# print(list_merge([[], [8, 8, 9], [0, 4], [1, 7], [1, 434, 65], [1]]))


def flatter_3(l):
    return [item for list_item in l for item in list_item]
