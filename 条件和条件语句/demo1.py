#!/usr/bin/env python3
name = input("What's your name?")
if name.endswith('shiwuhao'):
    if name.startswith('Mr.'):
        print('Hello Mr.shiwuhao')
    elif name.startswith('Mrs.'):
        print('Hello Mrs.shiwuhao')
    else:
        print('Hello shiwuhao')
else:
    print('Hello stranger')
