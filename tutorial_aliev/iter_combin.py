import itertools


n, k = map(int, input().split())

result = list(itertools.combinations(range(n), k))

print(len(result))