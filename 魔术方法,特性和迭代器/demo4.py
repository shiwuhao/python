# /usr/bin/env python3
def check_index(key):
    """
    指定的键是否是可接受的索引?
    键必须是非负整数,才是可接受的.如果不是整数,
    将引发TypeError异常;如果是负数,将引发IndexError异常(因为这个序列的长度时无穷的)
    :param key:
    :return:
    """
    if not isinstance(key, int): raise TypeError
    if key < 0: raise IndexError


class ArithmeticSequence:
    def __init__(self, start=0, step=1):
        """
        初始化这个算数序列
        :param start: 序列中的第一个值
        :param step: 两个相邻值的差
        changed: 一个字典,包含用户修改后的值
        """
        self.start = start
        self.step = step
        self.changed = {}

    def __getitem__(self, key):
        """
        从算数序列中获取一个元素
        """
        check_index(key)
        try:
            return self.changed[key]
        except KeyError:
            return self.start + key * self.step

    def __setitem__(self, key, value):
        """
        修改算数序列中的元素
        """
        check_index(key)
        self.changed[key] = value


s = ArithmeticSequence(1, 2)

print(s[1], s[2], s[3], s[4], s[5])  # 3 5 7 9 11

s[4] = 2
print(s.changed)  # {4: 2}
print(s[4])  # 2
print(s[5])  # 11
