from abc import ABC
from dataclasses import dataclass
from random import random


# ДОБАВИТЬ здесь и далее: документацию для классов, свойств и методов (кроме специальных)

@dataclass
class Film(ABC):
    name: str
    genre: str

    def __str__(self):
        return (f'{self.name}'
                f'\n{self.genre}')


@dataclass
# ОТВЕТИТЬ: как по-вашему переводится и что означает имя этого класса?
class Employes(Film):
    limitation_age: str = ''
    premiere_date: str = ''

    def __str__(self):
        return (f'{super().__str__()}'
                f'\n{self.limitation_age}'
                f'\n{self.premiere_date}')


@dataclass
class FilmCard(Employes):
    # КОММЕНТАРИЙ: все атрибуты класса, которые вы прописываете в датаклассе, так и остаются атрибутами класса, поэтому в случае с определением одноимённых методов возникает конфликт имён — когда в классе нам требуется прописать методы для управления полями (геттеры и сеттеры), мы используем свойства (@property) с нужными именами, а поля именуем как частные (_budget) или защищённые (__budget)
    budget: str = ''
    fees: str = ''
    reviews: str = ''
    rating: str = ''

    # ДОБАВИТЬ здесь и далее: аннотации параметров и возвращаемых значений методов

    # ИСПРАВИТЬ: все эти методы должны быть в классе фабрики
    def empl(self, age, data):
        self.limitation_age = age
        self.premiere_date = data

    def budgetet(self):
        self.budget = str(int(random() * 1_000_000)) + ' $'

    def feeses(self):
        self.fees = str(int(random() * 1_000_000)) + ' $'
        # ИСПОЛЬЗОВАТЬ: f-строки
        self.fees = f'{random()*1_000_000:.0f} $'

    def reviews_viewer(self, rew):
        self.reviews = rew

    def rating_random(self):
        self.rating = str(int(random() * 100))

    def __str__(self):
        return (f'{super().__str__()}'
                f'\nБюджет {self.budget}'
                f'\nСборы {self.fees}'
                f'\nОтзывы {self.reviews}'
                f'\nРейтинг {self.rating}')


class Factory:
    @staticmethod
    def create_film():
        film = FilmCard('Терминатор', 'Боевик')
        return film

    def hire_film(self, films):
        return films


# КОММЕНТАРИЙ: боюсь, у вас получилась объектная модель, которая не имеет отношения к шаблону Фабрика, да и в целом довольно бессмысленна — например, какую задачу решает разнесение полей, очевидно относящихся к одной карточке одного фильма, по нескольким классам?
# ОТВЕТИТЬ: на правах предположения: не путаете ли вы композицию с наследованием?

# СДЕЛАТЬ: переработайте свой код, оставьте один класс для карточки фильма и один класс для фабрики


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


# ИТОГ: переписать — 1/6
