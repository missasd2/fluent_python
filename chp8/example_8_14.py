"""
接受可变参数的风险
"""


class TwilightBus:

    def __init__(self, passengers=None):
        if passengers is None:
            self.passengers = [] # 当为None时，创建一个新的空列表
        else:
            self.passengers = passengers # 把self.passengers变成passengers的别名，而后者是传给__init__方法的实参的别名

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name) # 在self.passengers上调用 .remove()和 .append()方法会修改传给构造方法的那个列表


class TwilightBus_1:

    def __init__(self, passengers=None):
        if passengers is None:
            self.passengers = []
        else:
            # 校车实例会自己维护乘客列表； 传入参数值时，会把参数值的副本赋值给self.passengers
            # 直接把参数赋值给 实例变量(self.passengers)需要慎重考虑；可通过创建副本避免对参数的修改
            self.passengers = list(passengers)

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)

if __name__ == '__main__':
    basketball_team = ["Sue", "Tina", "Maya", "Diana", "Pat"]
    bus = TwilightBus(basketball_team)
    bus.drop("Tina")
    bus.drop("Pat")
    print(basketball_team) # 下车的学生从篮球队中消失了

    print("==============")
    basketball_team_1 = ["Sue", "Tina", "Maya", "Diana", "Pat"]
    bus1 = TwilightBus_1(basketball_team_1)
    bus1.drop("Tina")
    bus1.drop("Pat")
    print(basketball_team_1)
