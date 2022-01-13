"""
示例7-22
    示例7-2 中 registration.py 模块的删减版


装饰器工厂函数
    将参数传给他，返回一个装饰器，然后把它应用到要装饰的函数上

"""

registry = []


def register(func):
    print("running register(%s)"% func)
    registry.append(func)
    return func


@register
def f1():
    print("running f1")


if __name__ == '__main__':
    print("running main")
    print("register ->", registry)
    f1()
    pass