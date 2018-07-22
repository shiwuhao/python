# /usr/bin/env python3

f = open('somefile.txt', 'w')
print('First', 'line', file=f)
print('Second', 'line', file=f)
print('Third', 'line', file=f)

f.close()

lines = list(open('somefile.txt'))
print(lines)  # ['First line\n', 'Second line\n', 'Third line\n']

first, second, third = open('somefile.txt')
print(first)  # First line
print(second)  # Second line
print(third)  # Third line
