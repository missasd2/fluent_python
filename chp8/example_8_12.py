"""
不要使用可变对象，作为可选参数的默认值
"""


class HauntedBus:

    def __init__(self, passengers=[]):
        # 把self.passengers变成passengers的别名
        self.passengers = passengers

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)


if __name__ == '__main__':
    bus1 = HauntedBus(["Alice", "Bill"])
    print(bus1.passengers)
    bus1.pick("Charlie")
    bus1.drop("Alice")
    print(bus1.passengers) # ['Bill', 'Charlie']

    bus2 = HauntedBus()
    bus2.pick("Carrie")
    print(bus2.passengers) # ['Carrie']

    bus3 = HauntedBus()
    print(bus3.passengers) # ['Carrie'] # 为bus3赋值的为默认列表，但是默认列表不为空

    bus3.pick("Dave")
    print(bus2.passengers) # ['Carrie', 'Dave']

    print(bus2.passengers is bus3.passengers) # True
    print(bus1.passengers) # ['Bill', 'Charlie']

    """
    bus2 和 bus3 都是没有指定初始参数的示例，因此他们在本例中会共享同一个乘客列表；
    
    self.passengers 变成了 passengers参数默认值的别名；
    默认值在定义函数时计算（通常在加载模块时），因此默认值变成了函数对象的属性；
    
    因此通常使用None，作为接收可变值的参数的默认值；
    """