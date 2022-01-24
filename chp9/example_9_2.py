"""
Vector2d实例有多种表式形式
大概意思有以下几点：

__repr__正式，__str__ 非正式。
__str__主要由 str(),format()和print()三个方法调用。
若定义了__repr__没有定义__str__，那么本该由__str__展示的字符串会由__repr__代替。
__repr__主要用于调试和开发，而__str__用于为最终用户创建输出。
__repr__看起来更像一个有效的 Python 表达式，可用于重新创建具有相同值的对象（给定适当的环境）。
什么是正式？什么是非正式？光听文档上还是太抽象了，那我们就来看看几个 Python 内置对象的__repr__、__str__区别。
（PS：因为 Python 内置函数 repr() 和 str() 分别调用对象的__repr__和__str__，所以这边就用这两个函数来举例。）
"""

from array import array
import math


class Vector2d:
    typecode = "d" #类属性，在实例和字节序列之间转换时使用

    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    # 将实例变成可迭代对象，这样才能拆包x,y = my_vector
    def __iter__(self):
        return (i for i in (self.x, self.y))

    def __repr__(self):
        class_name = type(self).__name__
        return "{}({!r}, {!r}) ".format(class_name, *self)

    # 实例的字符串表示形式
    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return bytes([ord(self.typecode)]) + bytes(array(self.typecode, self))

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))


if __name__ == '__main__':
    v1 = Vector2d(3, 4)
    print(v1.x, v1.y)
    # 调用 __str__ 方法
    print(v1)
    print(str(v1))
    # 调用 __repr__ 方法
    print(repr(v1))