# Factory
Factory 設計模式的概念，是讓 Factory 來提供 Product， user 只需要知道使用 Factory 便可以得到需要的 Product，不需要知道實作/建立 Product 的細節

- 情境

    一個物流公司，初期只提供陸上物流，每次會分派卡車作為運輸體執行運輸，突然有天業務擴展需要支援海上物流，會分配輪船作為運輸體執行運輸，不過此時程式碼只有讓公司生產一種名叫卡車的運輸體 instance，而所有相關程式碼都是依賴該運輸體，所以如果要額外產生輪船運輸體 instance，得花時間拆解舊有邏輯以支援輪船運輸體類別。如果接下去的做法和過去相同，則日後公司只要每支援新的物流業務需要新的運輸體類別，就得在重新拆解邏輯，花上額外的成本


從程式面的角度來解釋，便是把 construct class instance 的動作封裝在 Factory (as a parent/super class)，由 Factory 專門 instantiate 這些 Product (as a subclass/child class)

幾個條件:
1. Factory as super/parent class to construct product(which is a sub/child class)
2. Product as sub/child class should 依賴共同 interface or abstract class
3. Each Product that create by Factory, should provide same method

Product 大致功能類別/架構相同，只有細節不同，便適合使用 Factory Pattern

- 優點
1. 不用在重複寫類似的 code (因為 Factory 有 common method，Product 依賴 common interface)
2. 符合 OCP，可以隨時擴充新的 Product 類別，不會修改到原始邏輯 (因為 Factory 依賴 Product interface，Concrete Product 依賴 common interface)
3. 符合 SRP，不同 Product 類別之間不會互相依賴，可以只專注修改特定 Product 細節 (因為 Concrete Product 依賴 common interface/ inherit base class)

- 缺點
1. 有時候 factory 會建立太多 interface or class，會造成程式碼太過多餘，當然也可以盡量將控制參數集中在一個 Factory(以下有兩個時作範例，剛好是兩種方式)

- 適合情境
  - 當無法預知 object 實際類別以及依賴關係
    
    基於 Factory 依賴 Product interface 的概念，實現隨時擴充新的 object，程式碼不影響其他 object 運作
    
    又或者 concrete Factory inherit base Factory，只修改實現新的程式碼

  - 希望 user 擴展 library or component
    
    基於 base Factory have common method and 依賴 Product interface/base class

    user 可以 inherit base Factory 修改方法細節，假使細節與建立新的 Product 有關，新的 Product 可以依賴 interface 或是 inherit base class 來實現

  - Reuse object to save resource 而不是重新建立 object (e.g., database, file system, network)

- 使用策略
  - 通常可以在初期使用，符合上述情境第一點，等到

- example
```python
class ConcreteProduct(Product):
    def _init__(*args):
        # detail attribute
        pass
    def do_something():
        # detail use case
        return
class Product:
    def do_something():
        pass
class CreatorFactory:
    def factory_method():
        # provide default/base implementation of factory method
        pass
    def common_method(*args):
        # creator main responsibility not for create product
        # it contain business logic that relies on product
        product = self.factory_method()
        product.do_something()


# there are 2 approach to make factory
# 1. external control parameter to decide user, tradeoff is too many condition need to handle, make code be ugly
class ProductGeneralFactory:
    def create_product(product_type):
        if product_type == "A":
            return ConcreteProduct("A")
        if product_type == "B":
            return ConcreteProduct("B")
        if product_type == "C":
            return ConcreteProduct("C")
    def common():
        product = create_product()
        product.do_something()

# 2. for each user type to declare new factory and product, it would be more accurately 準確和固定, but too 多餘
class ConcreteProductA(Product):
    def do_something():
        # modify some detail
        pass
class ConcreteCreatorA(CreatorFactory):
    def factory_method(*args) -> User:
        return ConcreteProductA()
def client(creator):
    creator.common_method()
client(ConcreteCreatorA)
```


## Simple Factory
Simple Factory Pattern (又被稱為 Static Factory Pattern)
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


## Abstract Factory

由來:
    因為 Simple Factory 在每次增加一個新的 Concreate Product時，都需要修改 Factory 的 create product 方法，來增加參數對應的物件，這違反了 OCP 原則
概念:
    將 Factory 抽象化，將 Simple Factory 只有一個 Factory class的設計方式，改為每一個獨立的物件都可以繼承 Factory abstract，實現專屬的 Factory class
    這樣每次增加一個 Product 時，便可以根據需要的 Product擴充 Product Factory來建立 Product 就行


當 Factory 每次增加一個類似 Product 類型的 element，同時也需要為其他 concrete Factory 增加該 element 的時候，便逐漸適合使用 abstract factory pattern