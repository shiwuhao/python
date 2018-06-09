# /usr/bin/env python3
def fibs(num):
    '返回斐波那契数列'
    result = [0, 1]
    for i in range(num - 2):
        result.append(result[-2] + result[-1])
    return result


print(fibs(10))
print(fibs.__doc__)
help(fibs)