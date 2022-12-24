from abc import ABC, abstractmethod


class Dish(ABC):

    def __init__(self, title, cost) -> None:
        super().__init__()
        self.title = title
        self.cost = cost

    @abstractmethod
    def dish1(self):
        pass

class Rassian_kitchen(Dish): 

    def __init__(self, title, cost) -> None:
        super().__init__(title, cost)

    def dish1(self):
        print(f'Блюдо русской кухни {self.title} готово')
        print(f'Цена {self.cost}')


class Georgian_kitchen(Dish):

    def __init__(self, title, cost) -> None:
        super().__init__(title, cost)

    def dish1(self):
        print(f'Блюдо грузинской кухни {self.title} готово')
        print(f'Цена {self.cost}')

class Factory(ABC):
    @abstractmethod
    def create_dish(self):
        pass

class RFactory(Factory):
    def create_dish(self, title, cost):
        return Rassian_kitchen(title, cost).dish1()

class GFactory(Factory):
    def create_dish(self, title, cost):
        return Georgian_kitchen(title, cost).dish1()

f = RFactory()
f.create_dish('Борщ', '200')

f = GFactory()
f.create_dish('Шашлык', '500')


'''Блюдо русской кухни Борщ готово
Цена 200
Блюдо грузинской кухни Шашлык готово
Цена 500'''