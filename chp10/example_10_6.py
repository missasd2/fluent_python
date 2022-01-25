"""
示例10-6

__repr__
    会被repr函数调用
    交互式命令行调用；
__str__:
    会被str、format、print函数调用
"""
import numbers
from array import array
import reprlib
import math


class Vector:
    typecode = "d"

    # self._components 是受保护的实例属性
    def __init__(self, components):
        self._components = array(self.typecode, components)

    # 构建一个迭代器，用于迭代
    def __iter__(self):
        return iter(self._components)

    # 使用reprlib.repr()函数来获取self._components 的有限长度表示形式
    def __repr__(self):
        components = reprlib.repr(self._components)
        components = components[components.find('['):-1]
        return "Vector({})".format(components)

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return (bytes([ord[self.typecode]])+
                bytes(self._components)
                )

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __abs__(self):
        return math.sqrt(sum(x * x for  x in self))

    def __bool__(self):
        return bool(abs(self))

    def __len__(self):
        return len(self._components)

    def __getitem__(self, index):
        cls = type(self)
        if isinstance(index, slice):
            a = cls(self._components[index])
            return cls(self._components[index])
        elif isinstance(index, numbers.Integral):
            return self._components[int(index)]
        else:
            msg = "{cls.__name__} indices must be integers"
            raise TypeError(msg.format(cls=cls))

    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(memv)


if __name__ == '__main__':
    v7 = Vector(range(7))
    print(repr(v7[1:4]))



