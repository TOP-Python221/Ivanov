import telebot 
from main_bd import index, save_chat
import requests
import json


db_command = index()[0]
db_text = index()[1]
bot = telebot.TeleBot('6473796616:AAE6MGyWgCg2CvMD5P5axLswBYvNnBA-VV0')

@bot.message_handler(commands=[db_command[1]])
def start(message):
    '''Команда /start'''
    
    m = message.from_user.first_name
    mes = db_text[1].format(name=m)
    save_chat(message.from_user.id, message.from_user.last_name, message.from_user.first_name, message.from_user.username, mes, message.text)
    bot.send_message(message.chat.id, mes)

@bot.message_handler(commands=[db_command[2]])
def pogoda(message):
    city = message.text.split()[-1].lower()
    api_url = 'https://api.api-ninjas.com/v1/weather?city={}'.format(city)
    response = requests.get(api_url, headers={'X-Api-Key': 'AuR2qI9zRfMqZ61glh3L2g==fLTmUWrOQOfsp82L'})
    if response.status_code == requests.codes.ok:
        temp = json.loads(response.text)
        t = temp['temp']
        gorod = city.title()
        mes = db_text[2].format(temper=t, city=gorod)
        save_chat(message.from_user.id, message.from_user.last_name, message.from_user.first_name, message.from_user.username, mes, message.text)
        bot.send_message(message.chat.id, mes)
    else:
        print("Error:", response.status_code, response.text)
        bot.send_message(message.chat.id, f'Некорректные данные')


    

@bot.message_handler(commands=[db_command[0]])
def help(message):
    mes = db_text[0].format(help=db_command[0], start=db_command[1], weather=db_command[2], news=db_command[3])
    save_chat(message.from_user.id, message.from_user.last_name, message.from_user.first_name, message.from_user.username, mes, message.text)
    bot.send_message(message.chat.id, mes)

@bot.message_handler(commands=[db_command[3]])
def news(message):
    r = requests.get('https://gnews.io/api/v4/top-headlines?category=general&lang=ru&country=ru&max=10&apikey=4e012121f28aa17b2c30893c7bbef732')
    news = r.content
    data = json.loads(news)
    data2 = data['articles'][0]
    title = data2['title']
    description = data2['description']
    url = data2['url']
    mes = db_text[3].format(title=title, description=description, url=url)
    save_chat(message.from_user.id, message.from_user.last_name, message.from_user.first_name, message.from_user.username, mes, message.text)
    bot.send_message(message.chat.id, mes)

bot.polling(none_stop=True)


#news
# https://gnews.io/api/v4/top-headlines?category=general&lang=ru&country=ru&max=10&apikey=4e012121f28aa17b2c30893c7bbef732
# 4e012121f28aa17b2c30893c7bbef732


#pogoda
# AuR2qI9zRfMqZ61glh3L2g==fLTmUWrOQOfsp82L


# , weather=db_command[2], news=db_command[3]


# t.me/itTelegrammProgerBot  -  ссылка на боты




