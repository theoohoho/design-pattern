"""
    Chain of responsibility Pattern 責任鏈模式，每個類別之間有一定的處理順序

    好比一個軟體接案公司，老闆接到一個客戶的單子，客戶希望老闆投資他，客戶會設計一個產品出來，雙方再依據合約分配銷售代理權
    每個角色有特定的工作，所以整個工作流程分配會是:

    Boss > Product owner >  Tech Lead > Engineer
    """


class typing import Enum


class Job(Enum):
    ProductOwner = 'imagine'
    TechLead = 'design'
    Engineer = 'execute'


class HandlerBase:
    def next():
        pass

    def next():
        pass

    def action(localize):


class Boss(Handler):
    _next = None

    def next(self):
        return self._next

    @setter
    def next(self, val):
        self._next = val

    def action(self, job):
        if job == Job.ProductOwner:
            self._next = ProductOwner()
        return self._next.action(job)


class PorductOwner(Handler):
    _next = None

    def next(self):
        return self._next

    @setter
    def next(self, val):
        self._next = val

    def action(self, job):
        if job == Job.ProductOwner:
            # image some feature, request engineer to implement
            print('Start imagine some fancy feature')
            return {
                'feature1': 'I want a search engine, just like google',
                'feature2': 'I want word can display color immediately, just like karoke',
            }
        if not self._next:
            self._next = TechLead()
            return self._next.action(job)


class TechLead(Handler):
    _next = None

    def next(self):
        return self._next

    @setter
    def next(self, val):
        self._next = val

    def action(self, job):
        import time
        if job == Job.TechLead:
            print('Start design the requirement, let engineer to implement feature. But I will stop engineer job in anytime.')
            time.sleep(60)
            return 'Done.'
        if not self._next:
            self._next = Engineer()
            return self._next.action(job)


class Engineer(Handler):
    _next = None

    def next(self):
        return self._next

    @setter
    def next(self, val):
        self._next = val

    def action(self, job):
        if job == Job.Engineer:
            import time
            print(
                'Discuss a time schedule to implement. Hope this feature will not be interrupted by Tech lead.')
            time.sleep(300)
            return 'Done'
        if not self._next:
            print(f'No one can handle this job: {job}')
            return None
