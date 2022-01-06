"""
示例7-19 使用缓存实现，速度更快

 lru(maxsize=128, typed=False)
  maxsize表示缓存多少个结果，
  typed如果为True会把不同参数类型的结果分开保存；
  lru_cache使用字典存储结果，因此所有参数必须是可散列的
"""

import functools

from example_7_16 import clock


@functools.lru_cache()
@clock # 叠放了装饰器 @lru_cache() 应用到@clock 返回的函数上
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == '__main__':
    print(fibonacci(10))