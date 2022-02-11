"""
Strategy Pattern 策略模式

當一個物件的行為，在不同情況下，會有不同實現方式

好比一個應用場景是，一個服務決定要使用 txt file 來保存 log 還是 Database來作為儲存載體
而這兩個策略，各有好壞，可以在適合的時機轉換使用，所以希望先建立一個通用模組，可以讓我們自由切換
"""

import datetime


class LoggerBase:
    def info(self) -> None:
        pass

    def debug(self) -> None:
        pass

    def warnning(self) -> None:
        pass

    def error(self) -> None:
        pass


class TextLogger(LoggerBase):
    def info(self, msg: str) -> None:
        print(f'LOGGER-INFO at {datetime.datetime.now()}: {msg}')

    def debug(self, msg: str) -> None:
        print(f'LOGGER-DEBUG at {datetime.datetime.now()}: {msg}')

    def warnning(self, msg: str) -> None:
        print(f'LOGGER-WARNING at {datetime.datetime.now()}: {msg}')

    def error(self, msg: str) -> None:
        print(f'LOGGER-ERROR at {datetime.datetime.now()}: {msg}')


class DBLogger(LoggerBase):
    def info(self, msg: str) -> None:
        print(f'DB LOGGER-INFO at {datetime.datetime.now()}: {msg}')

    def debug(self, msg: str) -> None:
        print(f'DB LOGGER-DEBUG at {datetime.datetime.now()}: {msg}')

    def warnning(self, msg: str) -> None:
        print(f'DB LOGGER-WARNING at {datetime.datetime.now()}: {msg}')

    def error(self, msg: str) -> None:
        print(f'DB LOGGER-ERROR at {datetime.datetime.now()}: {msg}')


class Worker:
    def __init__(self, logger):
        super().__init__()
        self.logger = logger

    def run(self):
        self.logger.info('Start service')


if __name__ == '__main__':
    
    worker = Worker(DBLogger())
    worker.run()