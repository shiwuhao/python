# /usr/bin/env python3
f = open('somefile.txt', 'r')
print(f.read(4))  # Hell   # 指定读取4个字符
print(f.read())  # o, World
f.close()
