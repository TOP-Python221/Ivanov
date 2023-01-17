from dataclasses import dataclass

import os



if os.name == 'nt':
    PATH_SEP = '\\'
else:
    PATH_SEP = '/'


@dataclass
class File:
    """Файл в файловой системе."""
    name: str
    dir: str
    
    @property
    def extension(self) -> str:
        return self.name.rsplit('.', 1)[-1]
    
    def ls(self) -> str:
        return f'{self.dir}{PATH_SEP}{self.name}'


class Folder(list):
    """Каталог в файловой системе. Может содержать вложенные каталоги и файлы."""
    def __init__(self, name: str, num: int = 5):
        super().__init__()      
        self.name = name
        self.num = num 
        for n in range(self.num):
            self += [File(f'текстовый документ{n}.txt', self.name)]

    def catalog(self, obj_folder: 'Folder', name, num):  
        self += [obj_folder(self.name + PATH_SEP + name, num)]
        
    def ls(self) -> str:
        if len(self) == 1:
            return self[0].ls()
        obj = self.pop(0)
        print(obj.ls())
        return self.ls()
        

def ls(*objects: File or Folder) -> str:      # оператор | выдает ошибку   нельзя сравнить type and type, так и не понял в чем дело
    for obj in objects:
        print(obj.ls())


f = File('dz.txt', 'Рабочая папка')
fol = Folder('новая папка', 5)

fol2 = Folder
fol3 = Folder

fol.catalog(fol2, 'курсы', 7)
fol.catalog(fol3, 'проекты', 7)

ls(f)
ls(*fol)

""" Рабочая папка\dz.txt
новая папка\текстовый документ0.txt
новая папка\текстовый документ1.txt
новая папка\текстовый документ2.txt
новая папка\текстовый документ3.txt
новая папка\текстовый документ4.txt
новая папка\курсы\текстовый документ0.txt
новая папка\курсы\текстовый документ1.txt
новая папка\курсы\текстовый документ2.txt
новая папка\курсы\текстовый документ3.txt
новая папка\курсы\текстовый документ4.txt
новая папка\курсы\текстовый документ5.txt
новая папка\курсы\текстовый документ6.txt
новая папка\проекты\текстовый документ0.txt
новая папка\проекты\текстовый документ1.txt
новая папка\проекты\текстовый документ2.txt
новая папка\проекты\текстовый документ3.txt
новая папка\проекты\текстовый документ4.txt
новая папка\проекты\текстовый документ5.txt
новая папка\проекты\текстовый документ6.txt """