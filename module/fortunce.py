# /usr/bin/env python3
import fileinput, random

fortunes = list(fileinput.input())
print(random.choice(fortunes))
