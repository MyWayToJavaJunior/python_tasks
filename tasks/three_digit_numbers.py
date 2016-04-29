#!/usr/bin/python3
"""
квадрат трехзначного числа оканчивается тремя цифрами, равными этому числу.
Найти и вывести все такие числа в порядке возрастания
"""


def three_digit():
    p = 0
    result = []
    for i in range(100, 999):
        p = i ** 2

        if str(i) == str(p)[-3:]:
            result.append(i)

    return result

print(three_digit())


# решение в одну строку
a = [x for x in range(100, 999) if str(x) == str(x**2)[-3:]]
print(a)

# Найти сумму всех четырехзначных чисел, сумма цифр каждого из
# которых равна 20
four_digit = [x for x in range(1000, 9999) if sum(int(x) for x in str(x)) == 20]
print(sum(four_digit))
