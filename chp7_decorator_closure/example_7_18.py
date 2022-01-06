"""
示例7-18 生成第n个斐波那契数，递归方式非常耗时
"""

from example_7_17 import clock


@clock
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-2) + fibonacci(n-1)


if __name__ == '__main__':
    print(fibonacci(10))