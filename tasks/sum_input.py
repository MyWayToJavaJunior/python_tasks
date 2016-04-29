#!/usr/bin/python3
# -*- coding: utf-8 -*-


def sum_input():
    n = int(input())
    sum = 0
    for i in range(n):
        sum += int(input())
    return sum

print(sum_input())
