"""
alex lewis 是别名，两个变量绑定的是同一个对象
charles，绑定的是不同的对象，虽然值是一样的, 但是他们的标识不同

is运算符：比较两个对象的标识（内存地址）
id（）函数：返回对象标识（内存地址）的整数形式表示；
"""

alex = {'name': 'Charles L', 'born': 1832, 'balance': 950}
lewis = alex
charles = {'name': 'Charles L', 'born': 1832, 'balance': 950}
print(alex is charles) # False ,证明两个变量引用的不是同一个对象

print(alex == charles) # True, 因为 dict类的__eq__ 方法就是这样实现的