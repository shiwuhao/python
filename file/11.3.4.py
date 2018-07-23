# /usr/bin/env python3
import fileinput


def process(string):
    print('Processing: ', string)


for line in fileinput.input():
    process(line)
