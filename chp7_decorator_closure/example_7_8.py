"""
示例7-8 average_oo.py 计算移动平均值的类
"""


class Averager():

    def __init__(self):
        self.series = []

    def __call__(self, new_value):
        self.series.append(new_value)
        total = sum(self.series)
        return total/len(self.series)


class Avenger_1():

    def __init__(self):
        self.series = []

    def __call__(self, new_value):
        self.series.append(new_value)
        total = sum(self.series)
        return total / len(self.series)


if __name__ == '__main__':
    avg = Averager()
    avg1 = Avenger_1()
    print(avg(10))
    print(avg(11))
    print(avg(12))
    ##
    print(avg1(10))
    print(avg1(11))
    print(avg1(12))
    pass
