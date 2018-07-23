# /usr/bin/env python3

def process(string):
    print('Processing: ', string, end='')


with open('file.txt') as f:
    while True:
        line = f.readline()
        if not line: break
        process(line)
