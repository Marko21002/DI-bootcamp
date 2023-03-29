leng = int(input())
multiplicator = '1'
total = 0


def calc(x, y, z):
    for i in range(y):
        res = x * int(z * i)
        total += res
    return (total)


calc(3, leng, multiplicator)
