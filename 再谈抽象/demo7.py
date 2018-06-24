# /usr/bin/env python3
from abc import ABC, abstractmethod


class Talker(ABC):
    @abstractmethod
    def talk(self):
        pass


class knigget(Talker):
    def talk(self):
        print(111)


k = knigget()
k.talk()

print(isinstance(k, Talker))


class Herring:
    def talk(self):
        print('Blub')


h = Herring()
h.talk()
print(isinstance(h, Talker))

print('------------------------')

Talker.register(Herring)
print(isinstance(h, Talker))
print(issubclass(Herring, Talker))
