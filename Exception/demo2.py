# /usr/bin/env python3
class MuffledCalculator:
    muffled = False

    def calc(self, expr):
        try:
            return eval(expr)
        except ZeroDivisionError:
            if self.muffled:
                print('Division by zero is illegal')
            else:
                raise


m = MuffledCalculator()
m.muffled = True
res = m.calc('1+2+3 / 0')
print(res)
