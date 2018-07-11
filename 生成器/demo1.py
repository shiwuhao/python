#!/usr/bin/env python3

def flatten(nested):
    for sublist in nested:
        for element in sublist:
            yield element


nested = [[1, 2], [3, 4], [5]]
print(flatten(nested))  # <generator object flatten at 0x10cb81fc0>

# 为使用所有的值 可对生成器进行迭代
for num in flatten(nested):
    print(num)

# 1
# 2
# 3
# 4
# 5

ls = list(flatten(nested))
print(ls)  # [1, 2, 3, 4, 5]
