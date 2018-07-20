# /usr/bin/env python3
f = open('./somefile.txt', 'r+')

for i in range(3):
    print(str(i) + ': ' + f.readline(), end='')

f.close()
