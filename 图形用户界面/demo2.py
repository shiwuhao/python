# /usr/bin/env python3

from tkinter import *


def callback(event):
    print(event.x, event.y)


top = Tk()
top.bind('<Button-1>', callback)
mainloop()
