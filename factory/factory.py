class Product:
    def get_info(self) -> dict:
        pass


class ConcreateProductA(Product):
    def __init__(self, name, p_type, price):
        self.name = name
        self.type = p_type
        self.price = price

    def get_info(self) -> dict:
        return {
            'name': self.name,
            'type': self.type,
            'price': self.price
        }


class ConcreateProductB(Product):
    def __init__(self, name, p_type, price):
        self.name = name
        self.type = p_type
        self.price = price

    def get_info(self) -> dict:
        return {
            'name': self.name,
            'type': self.type,
            'price': self.price
        }


class ProductEnum(enum):
    ProductA = 'A'
    ProductB = 'B'


class SimpleFactory:
    def __init__(self):
        pass

    @staticmethod
    def create_product(product: ProductEnum):
        product_collect = {
            ProductEnum.ProductA: ConcreateProductA('ProductA', 'drink', 100),
            ProductEnum.ProductB: ConcreateProductB('ProductB', 'food', 50)
        }
        return product_collect.get(product)


def simple_client():
    # Get Porduct A
    product = SimpleFactory.create_product(ProductEnum.ProductA)
    product.get_info()
