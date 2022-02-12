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