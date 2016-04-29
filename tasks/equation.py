#!/usr/bin/python3

# коэффициент при члене, содержащем переменную, опускается, если его модуль равен единице;
# член, коэффициент при котором равен нулю, опускается (кроме случая, когда все коэффициенты равны нулю, тогда
# трехчлен состоит из одной цифры 0);
# знак "+" опускается, если он предшествует отрицательному коэффициенту;
# знак "+" опускается, если он стоит в начале выражения (так называемый унарный плюс);
# знак умножения между коэффициентом и переменной опускается


def equation(k_list):

    a = k_list[0]
    b = k_list[1]
    c = k_list[2]
    result = ''

    if a == 0 and b == 0 and c == 0: # если все нули
        result = 0

    # A
    if a != 0:
        result = '' + str(a)

    # B
    if abs(b) == 1:
        if b > 0:
            result += '+x'
        else:
            result += '-x'
    elif b > 0:
        result += '+{}x'.format(b)
    elif b < 0:
        result += '{}x'.format(b)
    # C
    if abs(c) == 1:
        if c > 0:
            result += '+y'
        else:
            result += '-y'
    elif c > 0:
        result += '{}y'.format(c)
    elif c < 0:
        result += '{}y'.format(c)

    return result

print(equation([3, 4, 5]))  # 3+4x+5x
print(equation([0, 0, 0]))  # 0
print(equation([0, 0, 1]))  # y
print(equation([0, 1, 0]))  # x
print(equation([0, 1, 1]))  # x + y
print(equation([0, 0, -1]))  # -y
print(equation([0, -1, 0]))  # -x
print(equation([0, -1, -1]))  # -x -y
print(equation([1, 2, -3]))  # 1+2x-3y
print(equation([0, -2, -3]))  # -2x-3y
