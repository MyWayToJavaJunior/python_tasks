#!/usr/bin/python3
x = input().split()
xs = (int(i) for i in x)

# def even(x):
#     return x % 2 == 0

# even = lambda x: x % 2 == 0

evens = list(filter(lambda x: x % 2 == 0, xs))
print(evens)
