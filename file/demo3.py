# /usr/bin/env python3
f = open('somefile.txt', 'w')
f.write('01234567890123456789')
print(f.seek(5))  # 5
f.close()
