"""
共享传参
"""


def f(a, b):
    a += b
    return a


x = 1
y = 2
print(f(x, y))
print(x, y) # x, y没有变

a = [1, 2]
b = [3, 4]
print(f(a, b)) # [1, 2, 3, 4]; a变了
print(a, b) # [1, 2, 3, 4] [3, 4]

t = (10, 20)
u = (30, 40)
print(f(t, u))
print(t, u) # 元组t没变
