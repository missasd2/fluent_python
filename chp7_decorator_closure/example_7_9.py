"""
示例7-9 average.py 计算移动平均值的高阶函数

只有嵌套在其他函数中的函数才可能需要处理 不在全局作用域中的外部变量
"""


def make_averager():
    # series为make_averager函数的局部变量
    series = []

    # averager的闭包延伸到函数的作用域之外，包含内部自由变量series的绑定
    def averager(new_value):
        # 在averager（）函数中，series是自由变量；指未在本地作用域中绑定的变量
        series.append(new_value)
        total = sum(series)
        return total / len(series)

    return averager


if __name__ == '__main__':
    # 调用make_averager时，返回一个averager函数对象；
    # avg是内部函数
    avg = make_averager()
    # 每次调用averager时，他会把参数添加到系列值中，然后计算当前平均值
    print(avg(10))
    pass