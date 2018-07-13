#!/usr/bin/env python3
import shelve

s = shelve.open('test', writeback=True)
s['x'] = ['a', 'b', 'c']
s['x'].append('d')

print(s['x'])  # ['a', 'b', 'c', 'd']
