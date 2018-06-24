# /usr/bin/env python3
class Person:
    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def greet(self):
        print("Hello world! I'm {}.".format(self.name))


foo = Person()
bar = Person()
foo.set_name('shiwuhao')
bar.set_name('chenxiaoding')
foo.greet()
bar.greet()

print(foo.name)
bar.name = 'cxd'
bar.greet()

# 如果foo时Person实例,可将foo.greet()视为Person.greet(foo)的简写,但后者的多态性更低
Person.greet(foo)