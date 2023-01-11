from abc import ABC, abstractmethod


# ДОБАВИТЬ везде: аннотации типов параметров всех методов и возвращаемых значений всех не встроенных методов


# Passenger & Cargo Carriers
class Carrier(ABC):
    @abstractmethod
    def carry_military(self, items):
        pass

    @abstractmethod
    def carry_commercial(self, items):
        pass


# Military & Commercial Planes
class Plane(ABC):
    @abstractmethod
    def display_description(self):
        pass

    @abstractmethod
    def add_objects(self, new_objects):
        pass


class PassengerCarrier(Carrier):
    def carry_military(self, items):
        print(f'Пассажиры {items} ', end=' ')

    # ИСПРАВИТЬ: у вас реализации этих двух методов ничем не отличаются — два метода с разными именами и одинаковыми реализациями в одном классе не нужны — если два метода заявлено в условии задачи, то их реализации должны отличаться: хотя бы выводимым текстом в данном случае
    def carry_commercial(self, items):
        print(f'Пассажиры {items}', end=' ')


class CargoCarrier(Carrier):
    def carry_military(self, items):
        print(f'Грузы {items}')

    # ИСПРАВИТЬ: аналогично предыдущему классу
    def carry_commercial(self, items):
        print(f'Грузы {items}')


class MilitaryPlane(Plane):

    # КОММЕНТАРИЙ: принцип Моста заключается в том, чтобы дополнить данные одного класса данными любого другого из определённого набора — в ООП для этого используется агрегация
    # ДОБАВИТЬ: соответственно, вам нужно для этих классов составить конструктор, с помощью которого в атрибут текущего экземпляра сохранить экземпляр любого наследника Carrier — то есть из подклассов Plane пробросить мост к подклассам Carrier

    def display_description(self):
        # ИСПРАВИТЬ: а этот метод должен в свою очередь использовать сохранённый экземпляр подкласса Carrier и его методы
        print('доставил военный самолет')

    # ДОБАВИТЬ: реализацию метода
    def add_objects(self, new_objects):
        pass


# ИСПРАВИТЬ: аналогично предыдущему классу
class CommercialPlane(Plane):
    def display_description(self):
        print('доставил гражданский самолет')

    def add_objects(self, new_objects):
        pass


p = PassengerCarrier()
c = CargoCarrier()
mil = MilitaryPlane()
com = CommercialPlane()

p.carry_military('военные')
mil.display_description()
p.carry_commercial('гражданские')
com.display_description()

# ДОБАВИТЬ: тесты для грузового военного и грузового коммерческого самолётов


# В мустат загрузаю архив потому что .txt не загружается
# КОММЕНТАРИЙ: достаточно скопировать ссылку на репозиторий в поле комментария к ответу — при работе в репозитории в Журнал вообще не нужно загружать какие бы то ни было файлы


# stdout:

# Пассажиры военные  доставил военный самолет
# Пассажиры гражданские доставил гражданский самолет


# ИТОГ: выполнить работу над ошибками — 1/6
