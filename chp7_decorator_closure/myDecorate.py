"""

自定义装饰器
"""
import time


def clock(func):
    print("running start")
    time.sleep(5)
    print("running end")
    return func


@clock
def f3():
    print("running f3")


