# /usr/bin/env python3
class Bird:
    song = 'Squaawk!'

    def sing(self):
        print(self.song)


bird = Bird()
bird.sing()

birdsong = bird.sing
birdsong()

print(bird.song)
