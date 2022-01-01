"""
示例6-3 Order类和使用函数实现的折扣策略
"""

from collections import namedtuple

Customer = namedtuple("Customer", "name fidelity")

"""
没有抽象类
各个策略都是函数
策略对象通常是很好的享元（flyweight）
享元：
    是可共享的对象，可以同时在多个上下文中使用
    共享的好处在于，不必在每个新的上下文中使用相同的策略时不断创建新的具体策略对象；
    具体策略一般没有内部状态，只是处理上下文中的数据，因此一定要使用普通的函数
    
策略模式的缺点：
    运行时消耗
"""


class LineItem:
    def __init__(self, product, quantity, price):
        self.product = product
        self.quantity = quantity
        self.price = price

    def total(self):
        return self.price * self.quantity


class Order:  # 上下文
    def __init__(self, customer, cart, promotion=None):
        self.customer = customer
        self.cart = list(cart)
        self.promotion = promotion

    def total(self):
        if not hasattr(self, "__total"):
            self.__total = sum(item.total() for item in self.cart)
        return self.__total

    def due(self):
        if self.promotion is None:
            discount = 0
        else:
            discount = self.promotion(self)  # 计算折扣只需盗用self.promotion()函数
        return self.total() - discount

    def __repr__(self):
        fmt = "<Order total: {:.2f} due: {:.2f}>"
        return fmt.format(self.total(), self.due())


def fidelity_promo(order):
    """为积分为1000以上的顾客提供5%折扣"""
    return order.total() * .05 if order.customer.fidelity >= 1000 else 0


def bulk_item_promo(order):
    """单个商品为20个以上提供10%折扣"""
    discount = 0
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total() * .1
    return discount


def large_order_promo(order):
    """订单中的不同商品达到10个或以上时提供7%折扣"""
    distinct_items = {item.product for item in order.cart}
    if len(distinct_items) >= 10:
        return order.total() * .07
    return 0


"""
    示例6-5 best_promo 函数计算所有折扣，并返回额度最大的
    promos 是函数列表
"""
promos = [fidelity_promo, bulk_item_promo, large_order_promo]




def best_promo(order):
    """选择可用的最佳折扣"""
    return max(promo(order) for promo in promos)


"""
示例6-4
"""
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

    banana_cart = [
        LineItem("banana", 30, .5),
        LineItem("apple", 10, 1.5),
    ]
    print(Order(joe, banana_cart, bulk_item_promo))

    long_order = [
        LineItem(str(item_code), 1, 1.0) for item_code in range(10)
    ]

    """
    示例6-5 best_promo 函数计算所有折扣，并返回额度最大的
    """
    print(Order(joe, long_order, best_promo))


