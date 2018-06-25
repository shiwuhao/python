# /usr/bin/env python3
class Bird:
    def __init__(self):
        self.hungry = True

    def eat(self):
        if self.hungry:
            print('Aaaah ...')
            self.hungry = False
        else:
            print('No, thanks!')


class SongBird(Bird):
    def __init__(self):
        # 使用函数super
        super().__init__()
        self.sound = 'Squawk'

    def sing(self):
        print(self.sound)


b = Bird()
sb = SongBird()

b.eat()
sb.eat()