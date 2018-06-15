# /usr/bin/env python3
def factorial(n):
    result = n
    for i in range(1, n):
        result *= i
    return result


print(factorial(10))


def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(10))