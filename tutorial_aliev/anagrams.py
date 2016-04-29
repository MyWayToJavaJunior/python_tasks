#!/usr/bin/python3
# -*- coding: utf-8 -*-


# Метки
# O(n^2)
def anagramSolution1(s1, s2):
    alist = list(s2)

    pos1 = 0
    stillOk = True

    while pos1 < len(s1) and stillOk:
        pos2 = 0
        found = False

        # пока не нашли (found=false)
        while pos2 < len(alist) and not found:
            if s1[pos1] == alist[pos2]:
                found = True
            else:
                pos2 += 1

        if found:
            alist[pos2] = None # ставим метку
        else:
            stillOk = False

        pos1 += 1

    return stillOk


# print(anagramSolution1('abcd', 'dcba'))

# сортируй и сравнивай
# sort() - O(n^2) или O(nlogn), поэтому тут не O(n)


def anagramSolution2(s1, s2):
    alist1 = list(s1)
    alist2 = list(s2)

    alist1.sort()
    alist2.sort()

    pos = 0
    matches = True

    while pos < len(s1) and matches:
        if alist1[pos] == alist2[pos]:
            pos += 1
        else:
            matches = False

    return matches


# print(anagramSolution2('abcde', 'edcba'))


"""
anagramSolution3
Полный перебор - плохо( в данном случае)
если перебрать всех возможных строк из символов
s1 и посмотреть входит ли в него s2. 20!
"""

# Подсчитывай и сравнивай

def anagramSolution4(s1, s2):
    c1 = [0] * 26
    c2 = [0] * 26

    for i in range(len(s1)):
        pos = ord(s1[i]) - ord('a')
        c1[pos] = c1[pos] + 1

    for i in range(len(s2)):
        pos = ord(s2[i]) - ord('a')
        c2[pos] = c2[pos] + 1

    j = 0
    stillOk = True
    while j < 26 and stillOk:
        if c1[j] == c2[j]:
            j += 1
        else:
            stillOk = False

    return stillOk

print(anagramSolution4('apple','pleap'))