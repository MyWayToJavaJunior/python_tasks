#!/usr/bin/python3

"""
Чтобы предсказать судьбу человека, нумеролог берет время жизни человека в секундах, затем складывает все цифры
этого числа. Если полученное число состоит более чем из одной цифры, операция повторяется, пока в числе не
останется одна цифра. Затем по полученной цифре и числу операций, необходимых для преобразования числа в цифру
нумеролог предсказывает судьбу человека. Нумеролог плохо умеет считать, а числа, с которыми он работает, могут
быть очень большими. Напишите программу, которая бы делала все расчеты за него
"""


def numerologist(number):

    count = 0
    result = number

    while len(str(result)) > 1:

        result = sum(int(x) for x in str(result))
        count += 1

    return result, count


print(numerologist(1))
print(numerologist(10))
print(numerologist(99))
print(numerologist(1001))
