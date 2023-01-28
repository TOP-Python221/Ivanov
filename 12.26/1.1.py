from random import randrange as rr, choice as ch
from string import ascii_lowercase as alc
from abc import ABC, abstractmethod


class Test(ABC):
    @abstractmethod
    def positive(self):
        pass

    @abstractmethod
    def negative(self):
        pass

class TestCase:
    def __init__(self):
        self.messages = [
            ''.join(ch(alc) for _ in range(rr(3, 6))) 
            for _ in range(1000)
        ]
        self.numbers = [
            (rr(10, 100) for _ in range(rr(4,7))) 
            for _ in range(1000)
        ]
        self.msg: str = []
        self.nums: int = []
       
        
    def print_msg(self):
        msg = self.messages.pop()
        self.msg += [msg]
        print(f'Элемент {msg} удален из списка')
        

    def print(self):
        self.messages += [self.msg[-1]]
        print(f'Элемент {self.msg.pop()} добавлен в список')
        
    
    def sum_nums(self):             #чет я тут с генераторами намудрил
        nums = self.numbers.pop()
        n = sum(nums)
        self.nums += [n]
        print(f'Элемент {n} удален из списка')
        
    
    def summ(self):
        self.numbers += [self.nums[-1]]
        print(f'Элемент {self.nums[-1]} добавлен в список')

class TestMessage(Test):
    '''Реализация интерфейса для удаления и отмены удаления элементов print_msg'''
    def __init__(self, case: TestCase):
        self.case = case 

    def positive(self):
        self.case.print_msg()

    def negative(self):
        self.case.print()

class TestNums(Test):
    '''Реализация интерфейса для sum_num'''
    def __init__(self, case: TestCase):
        self.case = case 

    def positive(self):
        self.case.sum_nums()

    def negative(self):
        self.case.summ()

class Pult:
    '''Класс управления командами'''
    def __init__(self):
        self.__commands: list[Test] = []
        self.__history: list[Test] = []

    def set_commands(self, command: Test):   # список команд
        self.__commands += [command]

    def press_on(self):                        # исполнение команд
        com = self.__commands.pop(0)
        com.positive()
        self.__history += [com]

    def press_cancel(self):                     # история команд и ее исполнение
        if len(self.__history) != 0:
            self.__history.pop().negative()


pult = Pult()
case = TestCase()
tm = TestMessage(case)
tn = TestNums(case)

pult.set_commands(tm)
pult.press_on()
pult.press_cancel()

pult.set_commands(tn)
pult.press_on()
pult.press_cancel()
        

'''Элемент jhx удален из списка
Элемент jhx добавлен в список
Элемент 313 удален из списка
Элемент 313 добавлен в список'''