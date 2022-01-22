"""
比较classmethod 和 staticmethod的行为
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
    # 类方法第一个参数为类本身
    # 类方法一般用于定义备选构造方法
    print(Demo.klassmeth())
    print(Demo.klassmeth("spam"))
    ###
    print(Demo.statmeth())
    print(Demo.statmeth("spam"))
    pass
