
"""

装饰器：
    是可调用的对象
    参数是一个函数。
    装饰器可能会处理入参函数，然后把它返回，或者替换成另一个函数或可调用对象。
"""
def deco(func):
    def inner():
        print("running inner()")
    return inner # 函数deco返回inner函数对象


@deco
def target(): # 使用deco装饰target
    print("running target()")



if __name__ == '__main__':
    print()
    print(target()) # 调用被装饰的target其实会运行 inner。
    print(target) #

