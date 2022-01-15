"""
示例8-18 Cheese有个kind属性和标准的字符串表示形式
"""


class Cheese:

    def __init__(self, kind):
        self.kind = kind

    def __repr__(self):
        return "Cheese(%r)" % self.kind


if __name__ == '__main__':
    import weakref
    stock = weakref.WeakValueDictionary() # stock 是WeakValueDictionary实例
    catalog = [Cheese("Red Leicester"), Cheese("Tilsit"), Cheese("Brie"), Cheese("Parmesan")]


    for cheese in catalog:
        stock[cheese.kind] = cheese # stock把奶酪的名称 映射到 catalog中Cheese实例的弱引用上；

    # stock是完整的
    print(sorted(stock.keys())) # ['Brie', 'Parmesan', 'Red Leicester', 'Tilsit']

    # 删除catalog后，stock中的大多数奶酪都不见了
    del catalog
    # catalog临时变量 引用了对象，这可能会导致该变量的存在时间比预期长；
    print(sorted(stock.keys())) # ['Parmesan']

    del cheese # cheese是全局变量，除非显式删除，否则不会消失
    print(sorted(stock.keys())) # []
