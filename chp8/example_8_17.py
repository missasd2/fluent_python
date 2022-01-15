"""
示例8-17 弱引用是可调用的对象，返回的是被引用过的对象
"""

import weakref

a_set = {0, 1}
wref = weakref.ref(a_set)
print(wref)

print(wref()) # {0, 1}

print(wref() is None) # False
print(wref() is None) # False