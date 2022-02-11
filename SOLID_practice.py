"""Single Responsibility Principle單一職責原則

A class should have only one reason to change.

假設有一個 Worker 可以做到 train、test、build image、deploy 的功能，而每個功能都包裝在一個 Worker class 內
這會有一個問題是，假使今天需要針對整個 Worker 進行修正或新增邏輯時，我需要把整包 class 看仔細，才能找到我需要維護的地方，
而且在不斷開發的期間，程式碼會是不斷增加的，這對於日後進行維護時，會很花時間，因為沒辦法直覺找到需要修改的地方
所以 SRP 的目的在於，我要針對一個 module 進行修改時，因為功能職責明確拆分出去，我可以很快速地只找到一個地方(功能區塊)讓我修正

好處是可讀性變高，比較好維護，加上功能拆分出去的關係，要做到擴展也比較容易

# 全部縮再一起的設計

"""
# 針對每個功能，各自獨立成一個小模組，往後我只需要找到對應的功能模組進行修正就行

class Worker:
    def git_clone():
        native_clone()
    def train():
        git_clone()
    def test():
        git_clone()
    def build():
        git_clone()
    def deploy():
        git_clone()

# Solution 1: separate data and func
worker_info = {}
class Worker:
    def train():
        worker_info
        native_clone()
    def test():
        worker_info
        native_clone()
    def build():
        worker_info
        native_clone()
    def deploy():
        worker_info
        native_clone()

# Solution 2: FACADE pattern
class WorkerFACADE:
    def train():
        Worker().train()
    def test():
        Worker().test()
    def build():
        Worker().build()
    def deploy():
        Worker().deploy()

# Solution 3: FACADE pattern
class WorkerFACADE(Worker):
    def __init__(self,*args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        worker_info(**kwargs)
    def common():
    def core_func():

class Trainer:
    def train():
        WorkerFACADE().train()
class Tester:
    def test():
        WorkerFACADE().test()
class Buidler:
    def build():
        WorkerFACADE().build()
class Deployer:
    def deploy():
        WorkerFACADE().deploy()


""" Open-Close principle開關原則

Software entities (class, modules, functions, etc.) should be open for extension, but closed for modification.

根據上述
加新功能時，需要寫程式碼來擴充功能，而不是修改現有程式碼，比如刪除舊有程式碼，以新的取代

For example:
Worker Builder 進行 docker login 時，原本只需要透過 config json 來登入，但目前針對不同需求，原本的登入方式行不通，
需要透過另一種方法來登入，此時便可以擴充登入方式，讓 Builder 可以選擇以其中兩種方式來進行 docker login

OCP 好處是降低修改風險，不用破壞原有功能，只需要新增程式碼，就可以基於原本的邏輯擴充另外一條路線來實現新功能，相對問題也比較少。

而通常這類新增功能，進行擴充的情境，不一定在前期設計階段就會發覺，所以可以透過後期重構來讓程式碼結構設計更符合需求

"""
# 因為這些功能是的目的是相同的，只是實作方向不同，所以要嘛可以用 if else 來做一個 switch
# 不過會發現沒有遵守 SRP，因為這兩個方法各自都是一個職責
# 所以為了能夠達成 OCP 概念，可以將這兩個方法抽出一個共同的抽象，這個抽象只會有一個共同方法給予兩種登入方式繼承
# 而因為把兩個登入方式都獨立成各自的 class，所以也一同實現了 SRP


class Builder:
    def login():
        pass

    def build():
        docker_client = login()
        docker_client.images.build()
        docker_client.images.push()


class DockekLogin(Builder):
    def __init__():
        self.docker_client = docker.DockerClient()

    def login():
        pass


class DockerFromConfig(DockekLogin):
    def login():
        self.docker_client.login(
            username='', dockercfg='/path/to/docker/config/json')


class DockerFromPassword(DockekLogin):
    def login():
        self.docker_client.login(username='', password='')


docker_client = new DockerFromConfig()
docker_client.build()

"""Liskov substitution principle里氏替換原則

Subtypes must be substitutable for their base types
子類別必須可以取代父類別，而且取代的意義就在於，即便是替換成子類別，也要能夠執行父類別的方法，而且要做到不出現任何錯誤或異常

幾個實作要點:
- child class must implement the method of father class
- child class have own attritube and method
- Overwrite or implement father class, defined argument should same with e

好處是版本升級時可以好的兼容性，子類別應加修改都不影響其他子類別

child class should inherit father class, and can implement same function
"""
# 根據上述，原本各自建立 login 方法的實體，可以轉變為 Import 到 Builder，加上兩個登入方法是共同的 Father Class
# 所以可以直接在 Builder 內使用 Father class 的 method


class Builder:
    def login_docker(login_method: DockerLogin):
        return login_method.login()

    def build():
        docker_client = login_docker()
        docker_client.images.build()
        docker_client.images.push()


class DockekLogin:
    def __init__():
        self.docker_client = docker.DockerClient()

    def login():
        pass


class DockerFromConfig(DockekLogin):
    def login():
        self.docker_client.login(
            username='', dockercfg='/path/to/docker/config/json')


class DockerFromPassword(DockekLogin):
    def login():
        self.docker_client.login(username='', password='')


builder = new Builder(new DockerFromConfig())
builder.build()

"""Interface Segregation Principle

Clients should not be forced to depend on methods that they do not use.

好處是在需要多型的時後，適合使用 IsP來為類別實作對應方法

常見情境好比 Worker Tester 分成兩種測試時，比如 Regular testing 和 NLU testing，兩者大多方法都相同，只有差別在支援儲存 LOG的功能
你可以能會想那如果其中一個沒有支援儲存功能的話，把它當做 Exception 就好了不是嗎，但是這就會違反 Liscov principle，取代 Father class 也不應該要出錯的問題
class Tester(Worker):
    def test():
        Popen('test')
        pass
    def store_log():
        pass
class NLUTester(Worker):
    def test():
        Popen('nlu test')
        pass

"""
# 所以這邊會把特別例外的方法獨立成一個 class or interface，只有需要這個功能的模組，才需要引入它
# 這樣當有特殊功能需要執行時，可以指定唯有繼承那個功能模組的實體才可以執行特殊功能

# 注意: 如果是在物件類別沒有太多，但具有特例方法的前提下，ISP 是可以合理使用的模式
# 但是在物件類別多，而且特例方法也多的前提下，參照 ISP 會變成產生很多個 interface
# 多個物件類別需要繼承特例 interface，去 OVERWRITE特例方法，每個物件類別之間實現差不多的邏輯，
# 最後就會發生寫出很多重複程式碼的情況，這時候 ISP 就不是特別適合的設計

class Store:
    def store_log():
        pass


class Tester(Worker, Store):
    def test():
        Popen('test')
        pass

    def store_log():
        pass


class NLUTester(Worker):
    def test():
        Popen('nlu test')
        pass


class Runner:
    def test(job: Worker):
        job.test()

    def store_log(job: Store):
        job.store_log()


runner = new Runner()
runner.test(new Tester())
runner.test(new NLUTester())

runner.store_log(new Tester())
# NLUTester 沒有支援 store log 功能
runner.store_log(new NLUTester())
"""
5.  Dependency inversion principle
high level module should not depend on low level module，But should depend on  abstraction
high level module 不依賴 low level module，而是依賴抽象
Abstraction should not depend on details. Details should depend on abstractions.
抽象不依賴細節，細節依賴抽象

For example:
老闆 (high level) -> depend on -> 工程師(low level)

可以從工程師抽出一個抽象，工程師和老闆的關係是員工，所以抽出一個員工的抽象
老闆 -> depend on -> 員工(抽象)

而工程師是基於員工的關係所以會依賴抽象建立物件
員工(抽象) <- 工程師(細節)

整體來看
老闆 -> depend on -> 員工(抽象) <- depend on <- 工程師(細節)

# 常見錯誤的例子
class Boss:
    employee = []
    demand = []
    # 老闆想要員工是可以實現功能的，所以一開始設想只有工程師
    def recruit(employee):
        self.employee.append(employee)
    def add_demend(demand):
        self.demand.append(demand)

    def start_work():
        for i in self.employee:
            # engineer start coding
            i.coding([demand for demand in self.demand])

class Engineer:
    def planning(demand):
        print('start planning')

    def coding(demand):
        planning(demand)
        print('start coding')

# 但是今天因為覺得工程師設計太醜，所以想要有人來設計畫面，需要另外找設計師
# 但是設計師不會 coding，所以這就違反了 Liscov princiople，因為設計沒有 coding的功能
class Designer:
    def design(demand):
        print('start designing')
"""
# 最後結果可以看到 Boss 如果需要加入 Designer 的 instance 的話，會遇到 Designer class 沒有 coding function 可以執行的問題
# 所以根據 Dependency inversion principle，high module (Boss) should depned on Abstraction(可以抽象一個員工 Class)
# Abstraction(員工 Class) should depend on detail(工程師、設計師...)
# 而工程師和設計師實際上是繼承員工 Class，可以擴充 Employee的功能，並且在 recruit 內帶入的 argument 也必須是 Employee class，這也就遵守了 Liscov principle
# 可以取代父類別，並且執行上不會發生錯誤


class Boss
 employee = []
  demand = []
   # 老闆想要員工是可以實現功能的，所以一開始設想只有工程師

   def recruit(employee: Emploee):
        self.employee.append(employee)

    def add_demend(demand):
        self.demand.append(demand)

    def start_work():
        for i in self.employee:
            # employee start working
            i.working([demand for demand in self.demand])

# 抽象一個 Employee class


class Emploee:
    def relax():
        print('relax until next job coming')

    def working(demand):
        print('start working')
        pass


class Engineer(Employee):
    def planning(demand):
        print('start planning')
        self.schedule.append(demand)

    def coding():
        print('start coding')
        for i in self.schedule:
            print(f'handling {i} job...')

    def working(demand):
        planning(demand)
        coding()


class Designer(Emploee):
    def design(demand):
        print('start designing')

    def working(demand):
        design(demand)


# 將建立物件的控制權拉到外部建立，這種設計，又稱為控制反轉 Inversion of Control，並將外部建立好的物件引入模組，又被稱為 Dependency Injection 依賴注入
new Boss().recruit(new Employee())
