# как работает for
"""
lst = [1, 2, 3, 4, 5, 6]
book = {
    'title': 'The Langoliers',
    'author': 'Stephen King',
    'year_published': 1990
}
string = 'Hello, world!'

for i in lst:
    print(i)

# создается итератор
it = iter(lst)
while True:
    try:
        i = next(it)
        print(i)
    except StopIteration:
        break
"""

# создание своего итератора
"""
from random import random


class RandomIterator:
    def __init__(self, k):
        self.k = k
        self.i = 0

    def __next__(self):
        if self.i < self.k:
            self.i += 1
            return random()
        else:
            raise StopIteration

    def __iter__(self):
        return self
"""


class DoubleElementListIterator:
    def __init__(self, lst):
        self.lst = lst
        self.i = 0

    def __next__(self):
        if self.i < len(self.lst):
            self.i += 2
            return self.lst[self.i - 2], self.lst[self.i - 1]
        else:
            raise StopIteration


class MyList(list):
    def __iter__(self):
        return DoubleElementListIterator(self)


for i in MyList([1,2,3,4]):
    print(i)