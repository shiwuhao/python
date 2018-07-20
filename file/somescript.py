# /usr/bin/env python3
import sys

text = sys.stdin.read()
words = text.split()
wordcount = len(words)

print('WorldCount:', wordcount)