# 单例模式 - 懒汉


class Singleton:
    __instance = None

    def __init__(self):
        if not Singleton.__instance:
            print('__init__调用')
        else:
            print('对象创建', self.getInstance())

    @classmethod
    def getInstance(cls):
        if not cls.__instance:
            print('getInstance')
            cls.__instance = Singleton()
        return cls.__instance


s = Singleton()  # 类初始化，没有创建对象
print(hasattr(Singleton, 'instance'))
Singleton.getInstance()  # 在这里创建对象
# print(hasattr(Singleton, 'instance'))
s1 = Singleton()  # 对象已经创建
# print(hasattr(Singleton, 'instance'))

print(s)
print(s1)