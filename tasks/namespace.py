#!/usr/bin/python3
# -*- coding: utf-8 -*-


name_dict = {'None': [], 'global': ['None']}

def add(name, var):
    if name in name_dict:
        name_dict[name] += [var]
    else:
        print('This namespace does not exist')


def create(name, prev_name):
    if name in name_dict:
        print('This namespace already exists')
    else:
        name_dict[prev_name] += [name]
        name_dict[name] = [prev_name]


def get(name, var):
    if name in name_dict:
        ns = name_dict[name]
        flag = True
        while name != 'None':
            if var in ns:
                flag = False
                return name
            else:
                name = ns[0]
                ns = name_dict[ns[0]]

        return name

def main():
    n = int(input())

    for i in range(n):
        cmd = list(input().split())
        if cmd[0] == 'create':
            create(cmd[1], cmd[2])
        elif cmd[0] == 'add':
            add(cmd[1], cmd[2])
        elif cmd[0] == 'get':
            print(get(cmd[1], cmd[2]))

if __name__ == '__main__':
    main()
