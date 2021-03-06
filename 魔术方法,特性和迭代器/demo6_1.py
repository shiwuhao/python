# /usr/bin/env python3
class Rectangle:
    def __init__(self):
        self.width = 0
        self.height = 0

    def __setattr__(self, key, value):
        if key == 'size':
            self.width, self.height = value
        else:
            self.__dict__[key] = value

    def __getattr__(self, item):
        if item == 'size':
            return self.width, self.height
        else:
            raise AttributeError


r = Rectangle()
print(r.size)  # (0,0)

r.size = 150, 150
print(r.size)  # (150,150)
