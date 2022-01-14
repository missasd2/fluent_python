"""
创建对象后才会把变量分配给对象
"""


class Gizmo:
    def __init__(self):
        print("Gizmo id: %d" % id(self))


# 变量x，y所引用的对象是不同的实例
x = Gizmo()
z = Gizmo()
y = Gizmo() * 10 # 先创建一个新的Gizmo实例
dir() # 肯定不会创建变量y
