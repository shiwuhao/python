# /usr/bin/env python3
try:
    x = int(input('Enter the first number'))
    y = int(input('Enter the last number'))
    print(x / y)
except ZeroDivisionError:
    print("The last number cat't be zero")
except TypeError:
    print("That wasn't a number, was it?")
