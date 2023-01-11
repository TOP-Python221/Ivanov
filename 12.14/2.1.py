from abc import ABC, abstractmethod


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
        
    def carry_commercial(self, items):
        print(f'Пассажиры {items}', end=' ')


class CargoCarrier(Carrier):
    def carry_military(self, items):
        print(f'Грузы {items}')
        
    def carry_commercial(self, items):
        print(f'Грузы {items}')


class MilitaryPlane(Plane):
    def display_description(self):
        print('доставил военный самолет')

    def add_objects(self, new_objects):
        pass


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


# В мустат загрузаю архив потому что .txt не загружается


# stdout:

# Пассажиры военные  доставил военный самолет
# Пассажиры гражданские доставил гражданский самолет
