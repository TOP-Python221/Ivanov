import re


class TextParser:
    """Парсер текстовых данных в некой системе."""
    def __init__(self, text: str):
        tmp = re.sub(r'\W', ' ', text.lower())
        tmp = re.sub(r' +', ' ', tmp).strip()
        self.text = tmp

    
    def get_processed_text(self, processor) -> None:
        """Вызывает метод класса обработчика.
        
        :param processor: экземпляр класса обработчика
        """
        result = processor.process_text(self.text)
        print(*result, sep='\n')


class WordCounter: 
    """Счётчик частотности слов в тексте."""
    def __init__(self, text: str) -> None:
        """Обрабатывает переданный текст и создаёт словарь с частотой слов."""
        self.__words = dict()
        for word in text.split():
            self.__words[word] = self.__words.get(word, 0) + 1
            
    def get_count(self, word: str):
        """Возвращает частоту переданного слова."""
        return self.__words.get(word, 0)
        
    def get_all_words(self):
        """Возвращает словарь с частотой слов."""
        return self.__words.copy()


class Adapter(): 
    '''Адаптер обработчика'''
    def __init__(self, obj):
        self.obj = obj

    def process_text(self, text): # Реализация интерфейса обработчика, требуемого системой.

        words = self.obj(text)
        keys = words.get_all_words()
        list_keys = [i for i in keys]

      
        return sorted(list_keys, key=lambda x: words.get_count(x))
        
text = '''  Практический опыт показывает, что рамки и место обучения кадров способствует 
            повышению актуальности позиций, занимаемых участниками в отношении поставленных задач. 
            Повседневная практика показывает, что новая модель организационной деятельности напрямую 
            зависит от существующих финансовых и административных условий? Таким образом, социально-экономическое 
            развитие позволяет выполнить важнейшие задания по разработке существующих финансовых и административных условий.'''


pars = TextParser(text)
word = WordCounter
adapter = Adapter(word)
pars.get_processed_text(adapter)


'''практический
опыт
рамки
место
обучения
кадров
способствует
повышению
актуальности
позиций
занимаемых
участниками
в
отношении
поставленных
задач
повседневная
практика
новая
модель
организационной
деятельности
напрямую
зависит
от
таким
образом
социально
экономическое
развитие
позволяет
выполнить
важнейшие
задания
по
разработке
показывает
что
существующих
финансовых
административных
условий
и'''