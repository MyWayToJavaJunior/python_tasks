#!/usr/bin/python3

# алгоритм евклида(вроде) по нахождению наименьшего общего делителя
def gcd(m, n):
    while m % n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm % oldn
    return n


class Fraction:

    def __init__(self, top, bottom):
        if type(top).__name__ == 'int' and type(bottom).__name__ == 'int':
            if bottom < 0:
                top = -1 * top
                bottom = abs(bottom)
            common = gcd(top, bottom)
            self.num = top // common
            self.den = bottom // common
        else:
            print('Error, args is not integer')

    def getNum(self):
        return self.num

    def getDen(self):
        return self.den

    def __str__(self):
        return '{}/{}'.format(self.num, self.den)

    def __repr__(self):
        return self.num / self.den

    def __add__(self, other):
        newnum = self.num * other.den + self.den * other.num
        newden = self.den * other.den
        # common = gcd(newnum, newden)
        return Fraction(newnum, newden)

    def __radd__(self, other):
        newnum = self.num * other.den + self.den * other.num
        newden = self.den * other.den
        return Fraction(newnum, newden)

    def __sub__(self, other):
        newnum = self.num * other.den - self.den * other.num
        newden = self.den * other.den
        # common = gcd(newnum, newden)
        return Fraction(newnum, newden)

    def __eq__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        return firstnum == secondnum

    def __mul__(self, other):
        newnum = self.num * other.num
        newden = self.den * other.den
        # common = gcd(newnum, newden)
        return Fraction(newnum, newden)

    def __truediv__(self, other):
        newnum = self.num * other.den
        newden = self.den * other.num
        # common = gcd(newnum, newden)
        return Fraction(newnum, newden)

    def __lt__(self, other):
        firstnum = self.num // self.den
        secondnum = other.num // other.den
        return firstnum < secondnum

    def __gt__(self, other):
        firstnum = self.num // self.den
        secondnum = other.num // other.den
        return firstnum > secondnum

    def __ge__(self, other):
        firstnum = self.num // self.den
        secondnum = other.num // other.den
        return firstnum >= secondnum

    def __le__(self, other):
        firstnum = self.num // self.den
        secondnum = other.num // other.den
        return firstnum <= secondnum

    def __ne__(self, other):
        firstnum = self.num // self.den
        secondnum = other.num // other.den
        return firstnum != secondnum

    def __iadd__(self, other):
        newnum = self.num * other.den + self.den * other.num
        newden = self.den * other.den
        return Fraction(newnum, newden)

f1 = Fraction(1, -6)
f2 = Fraction(1, 12)
f1 += f2
print(f1)
print(f1 + f2)
print(f2 - f1)
print(f1 == f2)
print(f1 * f2)
print(f1 / f2)
print(f1 - f2)
print(f1 < f2)
print(f1 > f2)
print(f1 >= f2)
print(f1 <= f2)
print(f1 != f2)
print(f1.__repr__())
