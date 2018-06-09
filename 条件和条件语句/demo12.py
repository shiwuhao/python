#!/usr/bin/env python3
strings = ['abc', 'def', 'ghl', 'abc', 'def']
index = 0
for string in strings:
    if 'abc' in string:
        strings[index] = '[censored]'
    index += 1
print(strings)
