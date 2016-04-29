import datetime

data = list(map(int, input().split()))
data = datetime.date(data[0], data[1], data[2])

delta = datetime.timedelta(days=int(input()))

result = data + delta

# print(result.strftime('%Y %m %d'))
print('{} {} {}'.format(result.year, result.month, result.day))
