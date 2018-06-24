# /usr/bin/env python3
def search(sequense, number, lower=0, upper = None):
    if upper is None: upper = len(sequense) - 1
    if lower == upper:
        assert number == sequense[upper]
        return upper
    else:
        middle = (lower + upper) // 2
        if number > sequense[middle]:
            return search(sequense, number, middle + 1, upper)
        else:
            return search(sequense, number, lower, middle)


seq = [34, 67, 8, 123, 4, 100, 95]
seq.sort()
print(seq)

print(search(seq, 67))
