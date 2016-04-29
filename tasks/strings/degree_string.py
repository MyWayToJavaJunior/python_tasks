#!/usr/bin/python3
"""
Пусть задана строка s = s1s2...sn. Назовем ее k-ой (k > 0) степенью sk строку sk = s1s2 . . .sns1s2 .
. .sn......s1s2...sn (k раз). Например, третьей степенью строки abc является строка аbсаbсаbс.

Корнем k степени из строки s называется такая строка t (если она существует), что tk = s.

Ваша задача состоит в том, чтобы написать программу, находящую степень строки или корень из нее.
(abc, 3) -> abcabcabc
(abcdabcd, -2) -> abcd
(abcd, -4) -> NO SOlUTION
abcd abcd abcd (12)
"""


def degree_string(string, degree):
    s = string[:]
    d = int(len(s) / abs(degree))

    if degree > 0:
        return s * degree
    elif degree < 0 and len(s) % abs(degree) == 0:
        res = s[0:d]
        if res * abs(degree) == s:
            return res
        else:
            return 'NO SOLUTION'


print(degree_string('abc', 3))
print(degree_string('abcdabcd', -2))
print(degree_string('abcd', -4))
print(degree_string('abcd', -1))
print(degree_string('abcdabcdabcdabcd', -4))
