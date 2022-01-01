# from example_6_3 import promos
from example_6_3 import Customer, LineItem, Order, fidelity_promo
"""
示例6-7 内省模块的全局命名空间，构建promos列表
"""

promos = [globals()[name] for name in globals()
          if name.endswith("__promo") and name != "best_promo"
          ] # 过滤掉best_promo 本身防止无限递归


def getPromos():
    promos = []
    for item in globals().items():
        if item[0].endswith("_promo") and item[0] != "best_promo":
            promos.append(item[0])
    return promos


def best_promo(order):
    """
    选择可用的最佳折扣
    :param order:
    :return:
    """
    return max(promo(order) for promo in promos)


if __name__ == "__main__":
    joe = Customer("John Doe", 0)
    ann = Customer("Ann Smith", 1100)
    cart = [
        LineItem("banana", 4, .5),
        LineItem("apple", 10, 1.5),
        LineItem("watermelon", 5, 5.0),
    ]
    # 不必要在新建订单时实例化新的促销对象，函数拿来用即可
    print(Order(joe, cart, fidelity_promo))  # 只需把策略函数作为参数传入


    #######
    print(getPromos())