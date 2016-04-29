#!/usr/bin/python3
# -*- coding: utf-8 -*-
# найти последовательность

# s = '001011100001100000'
s = 'dddredaasddddddndddddddddddd'


def chain_letter(string, char):
    count = 0
    max_chain = 0
    result_chain = []
    for i, symbol in enumerate(string):

        if symbol == char:
            count += 1
            if i == len(string) - 1:
                if count > max_chain:
                    max_chain = count
                    result_chain.append(s[len(string)-count:])

        else:
            if count > max_chain:
                max_chain = count
                result_chain.append(string[i-count:i])

            count = 0

    return result_chain, max_chain

print(chain_letter(s, 'd'))
