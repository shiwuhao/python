# /usr/bin/env python3
class Fibs:
    def __init__(self):
        self.a = 0
        self.b = 1

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        return self.a

    def __iter__(self):
        return self


fibs = Fibs()

i = 1
for f in fibs:
    i += 1
    if f > 1000:
        print(i, f)
        break
