#!/usr/bin/env python3
from random import randrange

num = int(input('How many dice?'))
sides = int(input('How many sides per die?'))

sum = 0
for i in range(num): sum += randrange(sides) + 1
print('The result is ', sum)
