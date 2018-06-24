# /usr/bin/env python3
class Secretive:
    def __inaccessible(self):
        print("Bet you cant't see me ...")

    def accessible(self):
        print("The secret message is :")
        self.__inaccessible()


s = Secretive()
#s.__inaccessible()
s.accessible()

s._Secretive__inaccessible()