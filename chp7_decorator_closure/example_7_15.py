"""
示例7-15 一个简单的装饰器，输出函数的运行时间
"""

import time


def clock(func):

    def clocked(*args): # clocked（）函数接受任意个定位参数
        t0 = time.perf_counter()
        result = func(*args) # clocked的闭包中包含自由变量func
        elapsed = time.perf_counter() - t0
        name = func.__name__
        arg_str = ', '.join(repr(arg) for arg in args)
        print("[%0.8fs] %s(%s) -> %r" % (elapsed, name, arg_str, result))
        return result

    return clocked  # 返回内部函数，取代被装饰的函数
