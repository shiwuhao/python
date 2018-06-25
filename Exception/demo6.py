# /usr/bin/env python3
try:
    x = int(input('Enter the first number'))
    y = int(input('Enter the last number'))
    print(x / y)
except (ZeroDivisionError, TypeError, ValueError) as e:
    print(e)
