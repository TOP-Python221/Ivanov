# что то я не совсем с парсером разобрался...


import re

class HTMLTag:
    default_indent_spaces: int = 2

    def __init__(self, name: str, value: str = '', **kwargs):
        self.name = name
        self.attributes = ''
        if kwargs:
            for i in kwargs:
                self.i = kwargs[i]
                self.attributes += str(f' {i}="{self.i}" ')
        self.attributes = ''.join(f' {k}="{v}"' for k, v in kwargs.items())
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


class HTMLParser:
    """
    Строитель для пошаговой обработки HTML документа.
    """
    single: set[str] = {'area', 'base', 'br', 'col', 'command', 'embed', 'hr', 'img', 'input', 'keygen', 'link', 'meta', 'param', 'source', 'track', 'wbr'}

    def __init__(self, html_doc: str):
        self.html = html_doc

    def add_eol(self, before_value: bool = True):
        pattern = re.compile(r'<(!-- )?/?\w+.*?( --)?>', re.S)
        bf = '\n' if before_value else ''
        return HTMLParser(pattern.sub(rf'\n\g<0>{bf}', self.html))

    def optimize_eol(self) -> 'HTMLParser':
        pattern = re.compile(r'\n{2,10}')
        return HTMLParser(pattern.sub('\n', self.html))

    def delete_eol(self) -> 'HTMLParser':
        pattern = re.compile(r'>\s*<')
        return HTMLParser(pattern.sub('><', self.html))

    def delete_empty(self) -> 'HTMLParser':
        pattern = re.compile(r'<(?P<tag>\w+?)>\s*</(?P=tag)>', re.S)
        return HTMLParser(pattern.sub('', self.html))

    def delete_tags(self, *tags: str) -> 'HTMLParser':
        """Важно: теги контейнеры удаляются вместе со всем содержимым, включая любые вложенные теги!"""
        q = self.html
        for tag in set(tags) - self.single:
            pat_op = re.compile(rf'<{tag}.*?>.*?<(?P<slash>/?){tag}', re.S)
            pat_cl = re.compile(rf'</{tag}.*?>.*?<(?P<slash>/?){tag}', re.S)
            lt = len(tag)
            while mo := pat_op.search(q):
                if mo:
                    sl = 1 if mo['slash'] else 0
                    start, i = mo.start(), mo.end() - (lt + sl + 1)
                    c = 1
                    while True:
                        if mo := pat_op.match(q, i):
                            sl = 1 if mo['slash'] else 0
                            i = mo.end() - (lt + sl + 1)
                            c += 1
                        elif mo := pat_cl.match(q, i):
                            sl = 1 if mo['slash'] else 0
                            if c > 1:
                                i = mo.end() - (lt + sl + 1)
                            elif c == 1:
                                i += lt + 3
                            c -= 1
                        else:
                            i += lt + 3
                            c -= 1
                        if not c:
                            break
                    q = q[:start] + q[i:]

        for tag in set(tags) & self.single:
            pattern = re.compile(rf'<{tag}.*?>', re.S)
            q = pattern.sub('', q)

        return HTMLParser(q)

    def delete_attrs(self, *attrs: str, all: bool = False) -> 'HTMLParser':
        q = self.html
        if all:
            pattern = re.compile(r'<\w+?( .*?)?>', re.S)
            q = pattern.sub(r'<\g<name>>', q)
        else:
            for attr_key in attrs:
                pattern = re.compile(rf'\s+?{attr_key}=\".*?\"')
                q = pattern.sub('', q)
        return HTMLParser(q)


def html_doc():
    root = HTMLTag.create('div')
    root.sibling('li', 'File', scr='class_name', clas='hhhhhhhhhhh')\
    .sibling('li', 'Edit')\
    .sibling('li', 'view')\
    .nested('div', 'jjjjjjjj')\
    .nested('div', 'hhhhhhhhh')
    div = root.build()
    return f'{div}'

class Handler:
    def __init__(self, html_doc):
        self.html = html_doc
        self.pars = HTMLParser(self.html)

    def delet(self):
        self.html = self.pars.delete_eol().html
        return self.html

    def optim(self):
        self.html = self.pars.optimize_eol().html
        return self.html


    


html = html_doc()
handler = Handler(html)
print(handler.delet())
print('=======================')
print(handler.optim())















