"""
deepcopy函数，对于循环引用情况的处理
"""


a = [10, 20]
b = [a, 30]
a.append(b)
print(a)

