#!/usr/bin/python3
"""
#1 подобие операции 'in'
Умышленно добавляем искомый элемент в список,
тем самым уменьшаем время программы. Добавили проверку в конце
для того, чтобы не писать еще одно условие в цикл
используем while, потому что при for найдет последний
элемент, а не при первых вхождении

#2 подобие операции 'max'
#3 есть последовательность, например,
2 7 9 2 0 1 2 10 4
нужно найти максимум и предыдущий максимум
ответ: 10, 9
"""
#1
# arr = []
# x = 5
# arr.append(x)
# find = False
# f_ind = -1
# i = 0
# while (arr[i] != x):
#     i += 1
#     find = True
#     f_ind = i
# if find and (f_ind != len(arr) - 1):
#     print(искомый элемент)

#2
arr = []
# ma = float(-'Inf')
# ma = float(-'Inf')
# f_ind = -1
# find = False
# for i, elem in enumerate(arr):
#     if elem > ma
#         ma = elem
#         f_ind = i
#         find = True

#3

arr = [10, 9, 9, 2, 0, 1, 2, 1, 4]
m1 = arr[0]
m2 = float('-Inf')
for elem in arr:
    if elem > m1:
        m2 = m1
        m1 = elem
    elif elem > m2 and elem != m1:
        m2 = elem
print(m1, m2)
