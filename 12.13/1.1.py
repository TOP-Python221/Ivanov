# ДОБАВИТЬ здесь и далее: документацию для классов, свойств и методов (кроме специальных)

class ClassText:

    # ДОБАВИТЬ здесь и далее: аннотации параметров и возвращаемых значений методов

    def __init__(self, class_name = '', value = ''):
        self.class_name = class_name
        self.value = value
        # ДОБАВИТЬ: аннотацию атрибута
        self.__fields = []

    @property
    def fields(self):
        return self.__fields

    @fields.setter
    def fields(self, value):
        self.__fields += [value]

    def __str(self, n = 0):
        if n == 0:
            res = f'class {self.class_name}:\n' + ' '*4
            if len(self.fields) == 0:
                res += 'pass'
            else:
                res += 'def __init__(self):\n' + ' '*8
        else:
            # ДОБАВИТЬ: строковый литерал должен выводиться в кавычках
            res = f'self.{self.class_name} = {self.value}\n' + ' '*8
        # ИСПРАВИТЬ: не слишком удачно построена последовательность и логика проверок и выполнения — два раза проверяется длина списка self.__fields
        if self.__fields:
            for i in self.fields:
                res += i.__str(n + 1)
        return res

    def __str__(self):
        return self.__str()

    @staticmethod
    def create(name: str, value: str = ''):
        return HTMLBuilder(name, value)


class HTMLBuilder:
    def __init__(self, root, value: str = ''):
        if isinstance(root, ClassText):
            self.root = root
        elif isinstance(root, str):
            self.root = ClassText(root, value)
        else:
            raise TypeError('Не те параметры')

    def add_field(self, name: str, value: str = ''):
        # ИСПРАВИТЬ: объект используется только один раз, запись не длинная — нет смысла в создании отдельной переменной
        # ИСПРАВИТЬ: мне представляется довольно странной идея создавать объект для поля как экземпляр ClassText — разве класс и поле — это одно и то же? почему не достаточно сохранить нужным образом аргументы name и value в поле __fields исходного экземпляра ClassText?
        field = ClassText(name, value)
        self.root.fields = field
        return self

    def build(self):
        return self.root


text = ClassText.create('ClassName')\
                .add_field('name', 'Сергей')\
                .add_field('number', '1')\
                .add_field('age', '3')
print(text.build())


# ДОБАВИТЬ: закомментированную копию вывода программы в стандартный поток в результате выполнения


# ИТОГ: не рекомендую практиковать копирование без осмысления, доработайте задачу — 3/6
