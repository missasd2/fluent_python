"""
chp7.6 nonlocal生命
"""

"""
示例7-13 计算移动平均值的高阶函数，不保存所有历史值，但有缺陷

nonlocal关键字
    作用是把变量标记为自由变量，
    即使在函数中为变量赋予新值，闭包中保存的绑定会更新；
"""


# def make_averager():
#     # 1. count是数字、字符串、元组或任何不可变类型
#     count = 0
#     total = 0
#
#     def averager(new_value):
#         # 2. count+=1语句的作用：在函数定义体中为count赋值了，会把count变成局部变量
#         # count不再是自由变量，不会保存在闭包中
#         # 3. 使用不到1.处的闭包
#         count += 1
#         total += new_value
#         return total / count
#
#     return averager


def make_averager():
    count = 0
    total = 0

    def averager(new_value):
        nonlocal count, total
        count += 1
        total += new_value
        return total / count

    return averager


if __name__ == '__main__':
    avg = make_averager()
    print(avg(10))
    print(avg(11))
    print(avg(12))
    pass
