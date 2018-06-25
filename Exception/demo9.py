# /usr/bin/env python3
x = None
try:
    x = 1 / 0
except NameError:
    print("Unknown variable")
else:
    print("That went well")
finally:
    print("cleaning up ...")
    del x
