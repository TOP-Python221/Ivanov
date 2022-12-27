from abc import ABC
from dataclasses import dataclass
from random import random


@dataclass
class Film(ABC):
    name: str
    genre: str

    def __str__(self):
        return (f'{self.name}'
                f'\n{self.genre}')


@dataclass
class Employes(Film):
    limitation_age: str = ''
    premiere_date: str = ''

    def __str__(self):
        return (f'{super().__str__()}'
                f'\n{self.limitation_age}'
                f'\n{self.premiere_date}')


@dataclass
class FilmCard(Employes):
    budget: str = ''
    fees: str = ''
    reviews: str = ''
    rating: str = ''

    def empl(self, age, data):
        self.limitation_age = age
        self.premiere_date = data

    def budgetet(self):
        self.budget = str(int(random() * 1_000_000)) + ' $'

    def feeses(self):
        self.fees = str(int(random() * 1_000_000)) + ' $'

    def reviews_viewer(self, rew):
        self.reviews = rew

    def rating_random(self):
        self.reting = str(int(random() * 100))

    def __str__(self):
        return (f'{super().__str__()}'
                f'\nБюджет {self.budget}'
                f'\nСборы {self.fees}'
                f'\nОтзывы {self.reviews}'
                f'\nРейтинг {self.reting}')


class Factory:
    @staticmethod
    def create_film():
        film = FilmCard('Терминатор', 'Боевик')
        return film

    def hire_film(self, films):
        return films


f = Factory()
film = f.create_film()
film.empl('+18', '10.12.22')
film.budgetet()
film.feeses()
film.reviews_viewer('Хороший фильм')
film.rating_random()
film = f.hire_film(film)
print(film)


""" Терминатор 
Боевик  
+18 
10.12.22 
Бюджет 914844 $ 
Сборы 314943 $
Отзывы Хороший фильм 
Рейтинг 88 """

