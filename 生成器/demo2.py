#!/usr/bin/env python3

g = ((i + 2) ** 2 for i in range(2, 27))
print(next(g))  # 16
print(next(g))  # 25
print(next(g))  # 36

res = sum(i ** 2 for i in range(10000000000000))
print(res)  # 285
