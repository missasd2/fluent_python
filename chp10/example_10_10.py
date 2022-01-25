"""
实现__setattr__ 方法，改写类中设置属性的逻辑
"""



import numbers
from array import array
import reprlib
import math


class Vector:
    typecode = "d"
    shortcut_names = "xyzt"

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

    def __getattr__(self, name):
        cls = type(self)

        if len(name) == 1:
            pos = cls.shortcut_names.find(name)
            if 0 <= pos < len(self._components):
                return self._components[pos]
        msg = "{.__name__!r} object has no attribute {!r}"
        raise AttributeError(msg.format(cls, name))

    def __setattr__(self, name, value):
        cls = type(self)
        if len(name ) == 1: # 特别处理名称是单个字符的属性
            if name in cls.shortcut_names: # 如果name是xyzt中的一个，设置特殊的错误消息
                error = "readonly attribute {attr_name!r}"
            elif name.islower():
                error = "can't set attributes 'a' to 'z' in {cls_name!r}"
            else:
                error = ""
            if error:
                msg = error.format(cls_name=cls.__name__, attr_name=name)
                raise AttributeError(msg)
        # 默认情况：在超类上调用__setattr__ 方法，提供标准行为
        super().__setattr__(name, value)

    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(memv)


if __name__ == '__main__':
    v = Vector(range(5))
    print(repr(v))
    print(repr(v.x))
    v.x = 10
    print(v.x)
    print(repr(v))