# /usr/bin/env python3
class Foobar:
    def __init__(self, value=42):
        self.somevar = value


foo = Foobar('This is a constructor argument')
print(foo.somevar)
