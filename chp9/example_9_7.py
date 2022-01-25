"""
示例9-7 让Vector2d不可变
"""
from array import array
import math


class Vector2d:

    __slots__ = ('__x', '__y')
    typecode = "d"

    def __init__(self, x, y):
        # 使用两个前导下划线，将属性标记为私有的
        self.__x = float(x)
        self.__y = float(y)

    # 装饰器把读值方法标记为特性
    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def __hash__(self):
        return hash(self.x) ^ hash(self.y)

    def __iter__(self):
        return (i for i in (self.x, self.y))

    def __repr__(self):
        class_name = type(self).__name__
        return "{}(!r), {!r}".format(class_name, *self)

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return (bytes([ord(self.typecode)]) +
                bytes(array(self.typecode, self))
                )

    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(*memv)

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __format__(self, format_spec):
        if format_spec.endswith("p"):
            format_spec = format_spec[:-1]
            coords = (abs(self), self.angle())
            outer_fmt = "<{}, {}>"
        else:
            coords = self
            outer_fmt = "({}, {})"
        components = (format(c, format_spec) for c in coords)
        return outer_fmt.format(*components)



    def angle(self):
        return math.atan2(self.y, self.x)


if __name__ == '__main__':
    v1 = Vector2d(3, 4)
    v2 = Vector2d(3.1, 4.2)
    print(hash(v1), hash(v2))
    print(set([v1, v2]))

    """
    实例9-10 私有属性的名称会被“改写”
    """
    v1 = Vector2d(3, 4)
    print(v1.__dict__)
    pass


