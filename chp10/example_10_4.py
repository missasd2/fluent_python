"""
示例10-4 可切片的序列
"""

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

    # 10-4
    def __len__(self):
        return len(self._components)

    def __getitem__(self, index):
        return self._components[index]

    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(memv)


if __name__ == '__main__':
    v1 = Vector([3, 4, 5])
    print(len(v1))
    print(v1[0], v1[-1])
    v7 = Vector(range(7))
    print(v7[1:4])
    pass