#!/usr/bin/env python3

def flatten(nested):
    # 不迭代类似于字符串的对象
    try:
        for sublist in nested:
            for element in flatten(sublist):
                yield element
    except TypeError:
        yield nested


ls = [[[1], 2], 3, 4, [5, 6, 7], [[8, [9], 10]], 'qqqqq']
print(list(flatten(ls)))
