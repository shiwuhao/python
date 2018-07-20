# /usr/bin/env python3
list = [
    'This is a\n',
    'This is b\n',
    'This is c\n',
]
f = open('./somefile.txt', 'w+')
f.writelines(list)
f.close()
