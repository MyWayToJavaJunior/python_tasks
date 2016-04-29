from functools import partial
import operator as op
# x = int('1101', base=2)
# print(x)
# int_2 = partial(int, base=2)
# x = int_2('1101')
# print(x)

d = [
    ('Guido', 'van', 'Rossum'),
    ('Haskell', 'Curry'),
    ('John', 'Backus')
]

sort_by_last = partial(list.sort, key=op.itemgetter(-1))
print(d)
sort_by_last(d)
print(d)
