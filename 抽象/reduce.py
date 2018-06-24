# /usr/bin/env python3
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
from functools import reduce

res = reduce(lambda x, y: x + y, numbers)
print(res)
print(sum(numbers))
