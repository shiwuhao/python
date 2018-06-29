# /usr/bin/env python3
class CounterList(list):
    def __init__(self, *args):
        super().__init__(*args)
        self.counter = 0

    def __getitem__(self, item):
        self.counter += 1
        return super(CounterList, self).__getitem__(item)


cl = CounterList(range(10))
print(cl)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

cl.reverse()
print(cl)  # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

print(cl[1], cl[2])  # 8 7

print(cl.counter)  # 2
