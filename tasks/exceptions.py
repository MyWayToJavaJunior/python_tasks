# try:
#     x = [1, 2, 'hello', 7]
#     x.sort()
#     print(x)
# except TypeError:
#     print('Type error :(')
#
# print('I can catch')


# def f(x, y):
#     try:
#         return x / y
#     except (TypeError, ZeroDivisionError) as e:
#         print(type(e).__name__)
#         print(e)
#         print(e.args)
#
# print(f(5, 0))
# print(f(5, []))


# если не знаем какая ошибка


# def f(x, y):
#     try:
#         return x / y
#     except:
#         print('error')
#
#
# print(f(5, 0))
# print(f(5, []))

# def foo(x, y):
#     return x / y
#
# try:
#     foo(4, 0)
# except ZeroDivisionError as e:
#     print(type(e).__name__)
# except ArithmeticError as e:
#     print('ArithmeticError')
# except AssertionError as e:
#     print('AssertionError')
#


# class NonPositiveError(Exception):
#     pass
#
#
# class PositiveList(list):
#
#     def append(self, item):
#         if item > 0:
#             super(PositiveList, self).append(item)
#         else:
#             raise NonPositiveError('nope positive number')
#
# p = PositiveList()
#
# p.append(123)
# p.append(123)
# p.append(123)
# p.append(0)


class BadName(Exception):
    pass


def greet(name):
    if name[0].isupper():
        return 'Hello, ' + name
    else:
        raise BadName(name + ' is inappropriate name')

