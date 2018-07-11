#!/usr/bin/env python3

def repeater(value):
    while True:
        new = (yield value)
        if new is not None:
            value = new


r = repeater(42)
print(next(r))  # 42

r.send('Hello World!')
print(next(r))  # Hello World!

r.send('43')
print(next(r))  # 43


