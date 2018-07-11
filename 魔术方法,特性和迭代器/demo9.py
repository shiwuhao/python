# /usr/bin/env python3
class TestIterator:
    value = 0

    def __next__(self):
        self.value += 1
        if self.value > 10:
            raise StopIteration
        return self.value

    def __iter__(self):
        return self


ti = TestIterator()
print(list(ti))  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
