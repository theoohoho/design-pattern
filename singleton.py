"""
Singleton
一個類別只能實例化一個物件 (也可以說只能產生一個物件/instance)，並且會提供 access 該物件的統一方法
也就是說不管在哪個地方 access 的物件，都是同一個物件，適合應用在需要唯一物件的場景 e.g 資料庫連線物件

"""


class SingletonObject:
    # private attribute
    _instance = None

    def __init__(self):
        if SingletonObject._instance is not None:
            raise Exception('Object already created.')

        SingletonObject._instance = self
        self.id = id(self)

    @staticmethod
    def get_instance():
        if SingletonObject._instance is None:
            return SingletonObject()
        return SingletonObject._instance

    def get_id(self):
        return self.id


if __name__ == "__main__":
    obj = SingletonObject()
    print(obj.get_id)

    obj2 = SingletonObject.get_instance()
    print(obj2.get_id)

    obj3 = SingletonObject()
