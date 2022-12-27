# ДОБАВИТЬ здесь и далее: документацию для классов, свойств и методов (кроме специальных)
class HTMLTag:
    default_indent_spaces: int = 2

    def __init__(self, name: str, value: str = '', **kwargs):
        self.name = name
        self.attributes = ''
        if kwargs:
            for i in kwargs:
                self.i = kwargs[i]
                self.attributes += str(f' {i}="{self.i}" ')
        self.value = value
        self.__nested: list[HTMLTag] = []

    @property
    def nested(self):
        return iter(self.__nested)

    @nested.setter
    def nested(self, value: 'HTMLTag'):
        self.__nested += [value]

    def __str(self, indent_level: int):
        margin = ' ' * indent_level * self.default_indent_spaces
        eol = ''
        result = f'{margin}<{self.name}{self.attributes}>{self.value}'
        if self.__nested:
            for tag in self.nested:
                result += '\n' + tag.__str(indent_level + 1)
            eol = f'\n{margin}'
        result += f'{eol}</{self.name}>'
        return result

    def __str__(self):
        return self.__str(0)

    @staticmethod
    def create(name: str, value: str = ''):
        return HTMLBuilder(name, value)


class HTMLBuilder:
    def __init__(self, root, value: str = ''):
        if isinstance(root, HTMLTag):
            self.root = root
        elif isinstance(root, str):
            self.root = HTMLTag(root, value)
        else:
            raise TypeError('Не те параметры')

    def nested(self, name: str, value: str = '', **kwargs):
        tag = HTMLTag(name, value, **kwargs)
        self.root.nested = tag
        return HTMLBuilder(tag)

    def sibling(self, name: str, value: str = '', **kwargs):
        tag = HTMLTag(name, value, **kwargs)
        self.root.nested = tag
        return self

    def build(self):
        return self.root


root = HTMLTag.create('div')
root.sibling('li', 'File', scr='class_name', clas='hhhhhhhhhhh')\
    .sibling('li', 'Edit')\
    .sibling('li', 'view')\
    .nested('div', 'jjjjjjjj')\
    .nested('div', 'hhhhhhhhh')
div = root.build()
print(div)


# ДОБАВИТЬ: закомментированную копию вывода программы в стандартный поток в результате выполнения

