# 流畅的Python源码



## 9.6 可散列的Vector2d

将实例变成可散列

## 9.7 Python的私有属性和“受保护”属性

改写:
    类的属性使用两个前导下划线
    子类对该私有属性的定义会被存入实例的__dict__属性中；

私有属性和受保护属性：
    只是一种约定，并不能组织用户从外部修改这些属性

私有属性：
    self.__x

受保护属性:
    self._x


实例属性:
    存储在实例中名为__dict__的字典里

## 9.8 使用__slots__类属性节省空间

定义__slots__的方式：

## 9.9 覆盖类属性

类属性可以为实例属性提供默认值；

如果为不存在的实例属性赋值，会新建实例属性,同名类属性不受影响


## 10.3 协议和鸭子类型

Python的序列协议：
    只需要 __len__和__getitem__两个方法；

## 10.4 可切片的序列

内置的序列类型，切片得到的是各自类型的新实例；

### 10.4.1 切片原理
slice类，有start stop step三种数据属性，以及indices方法

S.indices(len) -> (start, stop, stride)
    给定长度为len的序列，计算S表示的扩展切片的起始和结尾索引，以及步幅;
    超出边界的索引会被截掉；
slice.indicies()方法
    能处理缺失索引、负数索引、长度超过目标序列的切片；

## 10.5 动态存取属性

属性查找机制：


## 10.6 散列和快速等值测试

# 11

抽象基类的常见用途： 实现接口时作为超类使用
除了抽象基类， 每个类都有接口：
