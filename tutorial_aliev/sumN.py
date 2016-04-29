import time


def timeSum(n):
    start = time.time()
    sumOfN(n)
    end = time.time()

    print('finish function sumOfN({}). time work - {}'.format(n, (end - start) * 100))


def sumOfN(n):
    return (n * (n + 1)) / 2



timeSum(10)
