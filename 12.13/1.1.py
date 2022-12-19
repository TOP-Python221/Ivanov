

class ClassText:
    def __init__(self, class_name = '', value = ''):
        self.class_name = class_name
        self.value = value
        self.__nested = []

    @property
    def nested(self):
        return self.__nested

    @nested.setter
    def nested(self, value):
        self.__nested += [value]
        
    def __str(self, n = 0):
        if n == 0:
            res = f'class {self.class_name}: \n    '
            if len(self.nested) == 0:
                res += 'pass'
            else:
                res += 'def __init__(self): \n        '
        else:
            res = f'self.{self.class_name} = {self.value}\n        '
        if self.__nested:
            for i in self.nested:
                #print(i, 111111111111)
                res += i.__str(n + 1)
        #res += f'{self.value}'
        
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
        word = ClassText(name, value)
        self.root.nested = word
        return self

    def bulid(self):
        return self.root

text = ClassText.create('ClassName').add_field('name', 'Сергей').add_field('number', '1').add_field('age', '3')

print(text.bulid())






