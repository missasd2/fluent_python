"""
chp7.4 变量作用域

Python不要求声明变量，但是假定在函数定义体中赋值的变量是局部变量；

"""
b = 3


def f1(a):
    print(a)
    print(b)  # 在函数内部调用全局变量


c = 6


def f2(d):
    print(d)
    """
    Python编译函数的定义体时，它判断c是局部变量，因为在函数中給它赋值了；
    Python会尝试从本地环境获取c；
    但是print语句尝试获取局部变量c的值时，发现调用的时候c没有绑定值；
    因此报错
    """
    #print(c)
    c = 9


d = 9
def f3(e):
    print("e: ", e)
    """
    使用global关键字声名变量d为全局变量
    """
    global d
    print("d: ", d)
    d = 999


if __name__ == '__main__':
    # f1(2)
    print(f3(12))

    """
    示例7-6 反汇编示例7-4中的f3函数
    """
    from dis import dis
    print(dis(f3))