from chp_7_4 import f3
"""
运行字节码的CPython VM是栈机器
"""

if __name__ == '__main__':
    # f1(2)
    print(f3(12))

    """
    示例7-6 反汇编示例7-4中的f3函数
    """
    from dis import dis

    print(dis(f3))