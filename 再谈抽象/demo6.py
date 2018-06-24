# /usr/bin/env python3
class Calculator:
    def calculate(self, expression):
        self.value = eval(expression)


class Talker:
    def talk(self):
        print('Hi, my value is ', self.value)


class TalkingCalculator(Calculator, Talker):
    pass


tc = TalkingCalculator()
tc.calculate('1+2*3')
tc.talk()

res = callable(getattr(tc, 'talk', None))
print(res)  # True

res = callable(getattr(tc, 'fnord', None))
print(res)  # False

setattr(tc, 'name', 'shiwuhao')
print(tc.name)  # shiwuhao

print(tc.__dict__)