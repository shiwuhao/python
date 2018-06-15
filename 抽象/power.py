# /usr/bin/env python3
def power(x, n):
    result = 1
    for i in range(n):
        result *= x

    return result


print(power(2, 3))


def power(x, n):
    if n == 0:
        return 1
    else:
        return x * power(x, n - 1)


print(power(2, 3))
