#!/usr/bin/python3
# система счисления


def system_number(num):
    if num == 0:
        raise ZeroDivisionError
    x = num
    result = []
    while num > 0:
        y = num % 2
        result.append(str(y))
        num = int(num / 2)

    b = ''.join(reversed(result))
    # a = bin(x)[2:]
    # if a == b:
    #     print(a, b, sep=' = ')
    return b


def eql_result(num1, num2, result):
    return int(system_number(num1), 2) * int(system_number(num2), 2) == result

print(eql_result(10, 10, 100))
