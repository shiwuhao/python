#!/usr/bin/env python3
strings = ['abc', 'def', 'ghl', 'abc', 'def']
for index,string in enumerate(strings):
    if 'abc' in string:
        strings[index] = '[censored]'
print(strings)
