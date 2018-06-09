#!/usr/bin/env python3
names = ['anne', 'beth', 'george', 'damon']
ages = [12, 45, 32, 102]
_list = list(zip(names, ages))
_dict = dict(zip(names, ages))
print(_list)
print(_dict)

for name, age in zip(names, ages):
    print(name, 'is', age, 'years old')
