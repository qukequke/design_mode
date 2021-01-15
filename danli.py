# 单例模式


class Singleton(object):

    def __new__(cls):
        if not hasattr(cls, 'instance'):  # 可以看到类有没有实例化对象
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance


if __name__ == '__main__':
    print(hasattr(Singleton, 'instance'))
    sin = Singleton()
    print(hasattr(Singleton, 'instance'))
    sin2 = Singleton()
    print(sin)
    print(sin2)
