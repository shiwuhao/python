# /usr/bin/env python3
from heapq import *
from random import shuffle

data = list(range(10))
shuffle(data)

heap = []
for n in data:
    heappush(heap, n)

print(heap)  # [0, 1, 2, 5, 3, 9, 4, 8, 7, 6]

heappush(heap, 0.5)  # [0, 0.5, 2, 5, 1, 9, 4, 8, 7, 6, 3]
print(heap)

print(heappop(heap))  # 0
print(heap)  # [0.5, 1, 2, 5, 3, 9, 4, 8, 7, 6]


