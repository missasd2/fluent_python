"""
示例7-16 使用clock装饰器
"""

import time
from example_7_15 import clock


@clock
def snooze(seconds):
    time.sleep(seconds)


@clock
def factorial(n):
    return 1 if n < 2 else n * factorial(n - 1)


if __name__ == '__main__':
    print(snooze(.123))
    print("6!= ", factorial(6))
    pass

