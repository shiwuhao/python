# /usr/bin/env python3
class MyClass2:
    def smeth():
        print('This is a static method')

    smeth = staticmethod(smeth)

    def cmeth(cls):
        print('This is a class method of ', cls)

    cmeth = classmethod(cmeth)


class MyClass:
    @staticmethod
    def smeth():
        print('This is a static method')

    @classmethod
    def cmeth(cls):
        print('This is a class method of ', cls)


MyClass.smeth()
MyClass.cmeth()
