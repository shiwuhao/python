# /usr/bin/env python3
while True:
    try:
        x = int(input('Enter the first number'))
        y = int(input('Enter the last number'))
        v = x // y
        print("x / y is ", v)
    except Exception as e:
        print("Invalid input, ", e)
        print('Please try again')
    else:
        break
