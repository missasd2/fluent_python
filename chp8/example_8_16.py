"""
示例8-16 没有指向对象的引用时，监视对象生命结束时的情形
"""

import weakref


s1 = {1, 2, 3}
s2 = s1


def bye():
    print("Gone with the wind")


ender = weakref.finalize(s1, bye) # 在s1 引用的对象上注册bye回调; finalize持有集合{1, 2, 3}的弱引用
print(ender.alive) # True ;  调用finalize 对象之前， .alive 属性的值为True

del  s1
print(ender.alive) # True # del不删除对象，而是删除对象的引用

s2 = "spam" # 重新绑定最后一个引用s2， 让集合{1, 2, 3}无法获取；对象被销毁了，调用了bye回调
print(ender.alive) # False; ender.alive属性变为了False

