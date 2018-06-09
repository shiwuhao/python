#!/usr/bin/env python3
result = []
for x in range(3):
    for y in range(3):
        result.append((x, y))

print(result)

girls = ['alice', 'bernice', 'clarice']
boys = ['chris', 'arnold', 'bob']
aa = [b + '+' + g for b in boys for g in girls if b[0] == g[0]]
print(aa)

girls = ['alice', 'bernice', 'clarice']
boys = ['chris', 'arnold', 'bob']
letterGirls = {}
for girl in girls:
    letterGirls.setdefault(girl[0], []).append(girl)
print(letterGirls)
aa = [b+'+'+g for b in boys for g in letterGirls[b[0]]]
print(aa)