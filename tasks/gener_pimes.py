import itertools


def primes():
    i = 2
    while True:
        print(i)
        if i == 2 or i == 3 or i == 5 or i == 7:
            yield i
        elif i % 2 != 0 and i % 3 != 0 and i % 5 != 0 and i % 7 != 0:
            yield i
        i += 1


print(list(itertools.takewhile(lambda x: x <= 31, primes())))
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
