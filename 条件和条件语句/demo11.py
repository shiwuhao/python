#!/usr/bin/env python3
strings = ['abc', 'def', 'ghl', 'abc', 'def']
for string in strings:
    if 'abc' in string:
        index = strings.index(string)
        strings[index] = '[censored]'
print(strings)