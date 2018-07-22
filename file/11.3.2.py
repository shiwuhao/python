# /usr/bin/env python3

def process(string):
    print('Processing: ', string)


# with open('file.txt') as f:
#     char = f.read(1)
#     while char:
#         process(char)
#         char = f.read(1)

with open('file.txt') as f:
    while True:
        char = f.read(1)
        if not char: break
        process(char)
