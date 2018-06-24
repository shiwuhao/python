# /usr/bin/env python3
class Filter:
    blocked = []

    def init(self):
        self.blocked = []

    def filter(self, sequence):
        return [x for x in sequence if x not in self.blocked]


class SPAMFilter(Filter):
    def init(self):
        self.blocked = ['SPAM']


f = Filter()
f.init()
res = f.filter([1, 2, 3])
print(res)  # [1, 2, 3]

s = SPAMFilter()
s.init()
res = s.filter(['SPAM', 'SPAM', 'SPAM', 'SPAM', 'eggs', 'bacon', 'SPAM'])
print(res)  # ['eggs', 'bacon']

print(issubclass(SPAMFilter, Filter))  # True

print(Filter.__bases__)  # (<class 'object'>,)

print(SPAMFilter.__bases__)  # (<class '__main__.Filter'>,)


print(isinstance(s, SPAMFilter))  # True
print(isinstance(s, Filter))  # True
print(s.__class__)  # <class '__main__.SPAMFilter'>



