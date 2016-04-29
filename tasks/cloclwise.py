# snail(array) => [1,2,3,6,9,8,7,4,5]

array = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

array1 = [
    [1, 2, 3, 1],
    [4, 5, 6, 4],
    [7, 8, 9, 7],
    [7, 8, 9, 7]
]
array2 = [
    [1, 2, 3, 1, 25],
    [4, 5, 6, 4, 12],
    [7, 8, 9, 7, 123],
    [7, 8, 9, 7, 57],
    [71, 84, 657, 123, 235]
]

# [4,5,6],
# [7,8,9]


def snail(array):
    res = []
    while True:
        try:
            res.extend(array.pop(0))

            for j in array:
                res.append(j.pop())

            s = array.pop()
            s.reverse()
            res.extend(s)

            for i in reversed(array):
                res.append(i.pop(0))
        except:
            break
    return res


print(snail(array2))

