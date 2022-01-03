"""
示例7-2 registration.py 模块

装饰器的特性：
    装饰器本身在导入模块时立即执行
    被装饰的函数只在明确调用时运行

装饰器的实际运用方式：
    1、装饰器通常在一个模块中定义，然后应用到其他模块中的函数上
    2、大多数装饰器会在内部定义一个函数，然后将其返回；
    3、多数装饰器会修改被装饰的函数，使用内部函数的代码需要靠闭包才能正确运作
"""

registry = [] #保存被@register装饰的函数引用


def register(func): # register的参数是一个函数
    print("running register(%s)" % func)
    registry.append(func)
    return func  # 必须返回函数


@register
def f1():
    print("running f1()")


@register
def f2():
    print("running f2()")


def f3():
    print("running f3()")


def main():
    print("running main")
    print("registry -> ", registry)
    f1()
    f2()
    f3()


if __name__ == '__main__':
    main()