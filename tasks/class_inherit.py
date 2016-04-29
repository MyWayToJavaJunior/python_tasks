#!/usr/bin/python3
# -*- coding: utf-8 -*-

class_dict = {}

def add(child, parents):
    if (len(parents) == 0) and (child not in class_dict):
        class_dict[child] = []
    elif child in class_dict:
        print('nope')
    else:
        # if child not in class_dict:
        class_dict[child] = parents
        # class_dict[child] += parents
        for i in parents:
            if i not in class_dict:
                class_dict[i] = []
            if len(class_dict[i]) > 0:
                for j in class_dict[i]:
                    if j not in class_dict[child]:
                        class_dict[child] += class_dict[i]
    for k, v in class_dict.items():
        if child in v:
            class_dict[k] += parents
"""
if child not in class_dict:
    class_dict[child] = parents
elif child in class_dict:
    print('nope')
    # class_dict[child] += parents
for i in parents:
    if i not in class_dict:
        class_dict[i] = []
    if len(class_dict[i]) > 0:
        for j in class_dict[i]:
            if j not in class_dict[child]:
                class_dict[child] += class_dict[i]
for k, v in class_dict.items():
if child in v:
    class_dict[k] += parents
    """


# def get(parent, child):


def main():
    n = int(input())

    for i in range(n):
        cmd = list(input().split())
        add(cmd[0], cmd[2:])
        print(class_dict)
    # q = int(input())
    #
    # for i in range(q):
    #     cmd = list(input().split())
    #
    #     print(get(cmd[0], cmd[1]))


if __name__ == '__main__':
    main()
