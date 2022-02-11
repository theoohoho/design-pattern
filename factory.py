"""
Factory 設計模式的核心概念，是讓 Factory 來實現物件的細節，使用者只需要知道使用 Factory 便可以得到需要的物件，不需要知道實現/建立物件的細節
程式上來講，便是把建立 class instance 的動作封裝在 Factory，由 Factory 專門 instantiate 這些 class
"""
"""Simple Factory Pattern (又被稱為 Static Factory Pattern)
概念:
    Simple Factory 有一個 Factory 和 Product，使用者只需要給予參數，便可以從 Factory 建立特定的 Product，並取得 Porduct (也就是由參數來決定 instance)

實際上:
    Simple Factory會有一個 Factory class, Product interface 和繼承 Product interface 的各種類型的 Concreate Product class
    Simple Factory class 可以 create 繼承相同 Product interface 的 Concreate Product class 的 instance

優點:
    Simple Factory 不用看程式碼，只需要知道參數帶入可以回傳哪些對應的結果
    這種模式搭配 config file，可以實現不用手動帶入程式碼參數，便可以自動切換不同環境的預設設定，減少不必要的複雜設定

缺點:
    每增加一個 ConcreateProduct，就得修改 CreateProduct 的方法，會違反 SOLID 的 OCP

"""


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


"""Abstract Factory
由來:
    因為 Simple Factory 在每次增加一個新的 Concreate Product時，都需要修改 Factory 的 create product 方法，來增加參數對應的物件，這違反了 OCP 原則
概念:
    將 Factory 抽象化，將 Simple Factory 只有一個 Factory class的設計方式，改為每一個獨立的物件都可以繼承 Factory abstract，實現專屬的 Factory class
    這樣每次增加一個 Product 時，便可以根據需要的 Product擴充 Product Factory來建立 Product 就行
"""


class FactoryAbstract:
    @staticmethod
    def create_product() -> Product:
        pass


class FactoryProductA(FactoryAbstract):
    @staticmethod
    def create_product() -> Product:
        return ConcreateProductA('ProductA', 'drink', 100)


class FactoryProductB(FactoryAbstract):
    @staticmethod
    def create_product() -> Product:
        return ConcreateProductB('ProductB', 'food', 50)


def abstract_client():
    # Get Porduct A
    product_a = FactoryProductA.create_product()
    product_a.get_info()
    # Get Porduct B
    product_b = FactoryProductB.create_product()
    product_b.get_info()


"""
Abstract Factory 另一種應用: Factory 有兩個 Product，需要支援不同裝置

e.g Gmail and Google Map 需要支援 Chrome, Safari
"""


class AbstractGoogleFactory:
    def create_gmail():
        pass

    def create_google_map():
        pass


class Product:
    def get_info(self):
        pass


class GoogleMap(Product):
    def __init__(self, device, support_data):
        self.name = 'google_map'
        self.support_data = support_data
        self.device = device

    def get_info(self):
        return {
            'name': self.name,
            'support_data': self.support_data,
            'device': self.device
        }


class Gmail(Product):
    def __init__(self, device, support_data):
        self.name = 'gmail'
        self.support_data = support_data
        self.device = device

    def get_info(self):
        return {
            'name': self.name,
            'support_data': self.support_data,
            'device': self.device
        }

class ChromeFactory(AbstractGoogleFactory):
    def create_gmail():
        return Gmail('chrome', datetime.datetime.now())

    def create_google_map():
        return GoogleMap('chrome', datetime.datetime.now())


class SafariFactory(AbstractGoogleFactory):
    def create_gmail():
        return Gmail('safari', datetime.datetime.now())

    def create_google_map():
        return GoogleMap('safari', datetime.datetime.now())


def abstract_client_():
    # setup chrome device support
    chrome_factory = ChromeFactory()
    chrome_gmail = chrome_factory.create_gmail()
    chrome_google_map = chrome_factory.create_google_map()

    # also can add safari factory to create product