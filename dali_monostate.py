'''
单例模式两种思路, 1种是 只产生一个对象，另1种是 单态模式 多对象共享状态
'''


# 通过将对象属性转到类属性上，强制让 对象一致
class Borg:
    # shared_state = {'1': '2'}
    shared_state = {}

    def __init__(self):
        self.x = 1
        self.__dict__ = self.shared_state
        # self.__dict__ = {}

    def a(self):
        pass


b = Borg()
b1 = Borg()
b.x = 4
print(b)
print(b1)
print(b.__dict__)
print(b1.__dict__)
