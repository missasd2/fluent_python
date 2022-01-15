"""
示例8-8 校车乘客在途中上车和下车
"""


class Bus:

    def __init__(self, passengers=None):
        if passengers is None:
            self.passengers = []
        else:
            self.passengers = list(passengers)

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)


if __name__ == '__main__':
    import copy
    bus1 = Bus(["Alice", "Bill", "Claire", "David"])
    # bus2为bus1的浅复制
    bus2 = copy.copy(bus1)
    # bus3为bus1的深复制
    bus3 = copy.deepcopy(bus1)
    print(id(bus1), id(bus2), id(bus3))

    bus1.drop("Bill")
    print(bus2.passengers)