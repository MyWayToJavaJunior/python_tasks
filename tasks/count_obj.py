#!/usr/bin/python3
# -*- coding: utf-8 -*-


# ans = 0
# alist = []
#
# for obj in objects:
#     if obj not in alist:
#         alist.append(obj)
#         ans += 1
#
# print(ans)

def closest_mod_5(x):

    found = False

    while not found:
        if x % 5 == 0:
            return x
        else:
            x += 1
    return "I don't know :("

