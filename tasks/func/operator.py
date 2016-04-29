import operator as op

x = [1, 2, 3]
f = op.itemgetter(1)  # f(x) == x[1]
print(f(x))

g = op.attrgetter('sort')  # f(x) == x.sort
# print(f([]))

d = [
    ('Guido', 'van', 'Rossum'),
    ('Haskell', 'Curry'),
    ('John', 'Backus')
]

d.sort(key=op.itemgetter(-1))
print(d)
