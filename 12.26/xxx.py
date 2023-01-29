from random import choice
from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class TextRequest:
    text: str 
    text_ans = ''


class Server:
    '''Эмитация ответов сервера'''
    def answer(self):
        return choice([200, 403, 404, 500])


class AnswerServer(ABC):
    '''Интерфейс обработчика ответов'''
    @abstractmethod
    def set_next_answer(self):
        pass

    @abstractmethod
    def execute(self):
        pass

class Respoun(AnswerServer):
    '''Реализация интерфейса обработчика ответа (общий)'''
    def __init__(self):
        self.__next_answer: AnswerServer = None

    def set_next_answer(self, answer: AnswerServer):
        self.__next_answer = answer
        return answer

    def execute(self, answer: Server):
        if self.__next_answer:
            return self.__next_answer.execute(answer)
        return ''


class Res200(Respoun):
    
    def execute(self, answer: Server, text: TextRequest):
        if answer == 200:
            text.text_ans = text.text[::-1]
            return f'Команда выполнена, {text.text_ans}' 
        else:
            return super().execute(answer) 

class Res403(Respoun):
    def execute(self, answer: Server, text: TextRequest):
        if answer == 403:
            text.text_ans = 'Ошибка сервера 403'
            return text.text_ans 
        else:
            return super().execute(answer)    


class Res404(Respoun):
    def execute(self, answer: Server, text: TextRequest):
        if answer == 404:
            text.text_ans = 'Ошибка сервера 404'
            return text.text_ans 
        else:
            return super().execute(answer)   


class Res500(Respoun):
    def execute(self, answer: Server, text: TextRequest):
        if answer == 500:
            text.text_ans = 'Ошибка сервера 500'
            return text.text_ans 
        else:
            return super().execute(answer) 

text = TextRequest('Привет')       
server = Server()
ans_serv = server.answer()


r200 = Res200().execute(ans_serv, text)
r403 = Res403().execute(ans_serv, text)
r404 = Res404().execute(ans_serv, text)
r500 = Res500().execute(ans_serv, text)

print(text.text_ans)


'Ошибка сервера 500'



'ЗАМЕТКА: все ответы сервера рандомны, при коде ответа 200 текст запроса переворачивается'