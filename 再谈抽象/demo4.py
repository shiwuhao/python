# /usr/bin/env python3
class MemberCounter:
    members = 0

    def init(self):
        self.members += 1


m1 = MemberCounter()
m1.init()
print(MemberCounter.members)  # 0
print(m1.members)  # 1

m2 = MemberCounter()
m2.init()
print(MemberCounter.members)  # 0
print(m2.members)  # 1
