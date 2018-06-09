#!/usr/bin/env python3
from math import sqrt
for n in range(99, 0, -1):
    root = sqrt(n)
    # print(root)
    if root == int(root):
        print(n)
        # break
