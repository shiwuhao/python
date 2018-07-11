# /usr/bin/env python3

from functools import reduce

my_sets = []
for i in range(10):
    tmp = set(range(i, i + 5))
    my_sets.append(tmp)

new_set = reduce(set.union, my_sets)

print(new_set)  # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13}
