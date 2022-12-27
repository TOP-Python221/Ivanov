from abc import ABC, abstractmethod

# ДОБАВИТЬ здесь и далее: документацию для классов, свойств и методов (кроме специальных)

class Dish(ABC):
    def __init__(self, title, cost) -> None:
        # УДАЛИТЬ: нет необходимости вызывать родительский конструктор в базовом классе
        super().__init__()
        self.title = title
        self.cost = cost

    @abstractmethod
    def dish1(self):
        pass


# ИСПРАВИТЬ: один класс наследник Dish — это одно конкретно взятое блюдо, например, борщ, пельмени, долма, шурпа, суши, гамбургер и так далее
class RussianKitchen(Dish):
    # УДАЛИТЬ: когда вам не нужно изменять поведение конструктора в дочернем классе, то вы можете просто не переопределять в дочернем классе метод __init__() и тогда для экземпляра этого класса будет использоваться конструктор родительского класса
    def __init__(self, title, cost) -> None:
        super().__init__(title, cost)

    def dish1(self):
        print(f'Блюдо русской кухни {self.title} готово')
        print(f'Цена {self.cost}')


class GeorgianKitchen(Dish):
    def __init__(self, title, cost) -> None:
        super().__init__(title, cost)

    def dish1(self):
        print(f'Блюдо грузинской кухни {self.title} готово')
        print(f'Цена {self.cost}')


class Factory(ABC):
    @abstractmethod
    # ИСПРАВИТЬ: сигнатура (имя, параметры, типы) абстрактного метода должна соответствовать сигнатурам методов реализаций
    def create_dish(self):
        pass


# ИСПРАВИТЬ: а конкретные реализации абстрактной фабрики могут быть использованы для группового создания экземпляров разных блюд, объединённых принадлежностью к конкретной кухне
class RFactory(Factory):
    def create_dish(self, title, cost):
        return RussianKitchen(title, cost).dish1()


class GFactory(Factory):
    def create_dish(self, title, cost):
        return GeorgianKitchen(title, cost).dish1()


f = RFactory()
f.create_dish('Борщ', '200')

f = GFactory()
f.create_dish('Шашлык', '500')


'''Блюдо русской кухни Борщ готово
Цена 200
Блюдо грузинской кухни Шашлык готово
Цена 500'''


# СДЕЛАТЬ: судя по моим наблюдениям у вас не больно-то хорошо закрепилось в памяти ООП — настоятельно рекомендую посмотреть мои соответствующие лекции по этому блоку (найдёте в ленте или в файлах группы в Teams)


# ИТОГ: переписать — 2/6
