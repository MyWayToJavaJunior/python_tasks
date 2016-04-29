#!/usr/bin/python3

"""
определим количество элементарных операций
"""

s = 0
p = 1
op_count = 0

for i in range(1, 1001):

    s += i
    op_count += 1
    p *= i
    op_count += 1

print('s = {}, p = ..., количество операций = {}'.format(s, op_count))
