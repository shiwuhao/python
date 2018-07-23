# /usr/bin/env python3

def process(string):
    print('Processing: ', string)


with open('file.txt') as f:
    for char in f.read():
        process(char)


with open('file.txt') as f:
    for line in f.readlines():
        process(line)
