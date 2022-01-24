"""
示例
classmethod装饰器
    定义操作类的方法；
    常用于定义备选构造方法


staticmethod装饰器
    普通函数，在类的定义体中，不是定义在模块层中；
"""


class Demo:
    @classmethod
    def klassmeth(*args):
        return args

    @staticmethod
    def statmeth(*args):
        return args

if __name__ == '__main__':
    """
    (<class '__main__.Demo'>,)
    (<class '__main__.Demo'>, 'spam')
    ()
    ('spam',)
    """
    # klassmeth 返回全部位置参数；
    # klassmeth 第一个参数始终是Demo类
    print(Demo.klassmeth())

    print(Demo.klassmeth("spam"))
    print(Demo.statmeth())
    print(Demo.statmeth("spam"))
    pass