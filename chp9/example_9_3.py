"""
备选构造方法
"""
import math
from array import array


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

    # 从字节序列转换成Vector2d实例
    """
    类方法使用classmethod装饰器修饰
    """
    @classmethod
    # 通过cls传入类本身
    def frombytes(cls, octets):
        # 从第一个字节读取typecode
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(*memv)



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