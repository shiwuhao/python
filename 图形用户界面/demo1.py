# /usr/bin/env python3

from tkinter import *


def clicked():
    print('I was clicked')


top = Tk()
btn = Button(text='Click me', command=clicked).pack()
# btn.config(text='Click me', command=clicked)
mainloop()
