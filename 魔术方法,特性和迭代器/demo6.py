# /usr/bin/env python3
class Rectangle:
    def __init__(self):
        self.width = 0
        self.height = 0

    def set_size(self, size):
        self.width, self.height = size

    def get_size(self):
        return self.width, self.height

    size = property(get_size, set_size)


r = Rectangle()
r.width = 10
r.height = 5
print(r.size)  # (10, 5)

r.size = 150, 150
print(r.width)  # 150
