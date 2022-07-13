import requests
from bs4 import BeautifulSoup as bs
import random
import telebot
from telebot import types

import os

URL = 'https://www.anekdot.ru/last/anekdot/'

API_KEY = str(open('/home/nelud/KEY/API_KEY_BOT.txt', 'r').read()).strip()

# https://openweathermap.org/

APPID = str(open('/home/nelud/KEY/API_KEY_WEATHER.txt', 'r').read()).strip()


def parser_jokes(url):
    request_web = requests.get(url)
    soup = bs(request_web.text, 'html.parser')
    anekdots = soup.find_all('div', class_='text')
    return [item.text for item in anekdots]

def parser_weather(city):
    try:
        request_web = requests.get("http://api.openweathermap.org/data/2.5/weather",
                    params={'q': city, 'type': 'like', 'units': 'metric', 'lang': 'ru', 'APPID': APPID})
        data = request_web.json()
        return data
    except Exception as e:
        print("Exception (find):", e)
        pass

list_of_jokes = parser_jokes(URL)
random.shuffle(list_of_jokes)

bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands=['start'])
def hello(m, res=False):

        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton("Новый анекдот")
        item2=types.KeyboardButton("Погода")
        markup.add(item1, item2)
        bot.send_message(m.chat.id, 'Нажми: ',  reply_markup=markup)

@bot.message_handler(content_types=['text'])
def jokes(message):

    if message.text.strip() == 'Новый анекдот' :
        bot.send_message(message.chat.id, list_of_jokes[0]) 
        del list_of_jokes[0]

    #Astrakhan,RU ||Moscow,RU || Petersburg,RU ||Kostanay, KZ
    elif message.text.strip() == 'Погода': 
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn_Moscow = types.KeyboardButton("Москва")
        btn_Piter = types.KeyboardButton("Санкт-Петербург")
        btn_Astra = types.KeyboardButton("Астрахань")
        btn_return = types.KeyboardButton("Назад")
        markup.add(btn_Moscow, btn_Piter, btn_Astra, btn_return)
        bot.send_message(message.chat.id, text="Выбери город", reply_markup=markup)


    elif message.text.strip() == 'Москва': 
        request_web = requests.get("http://api.openweathermap.org/data/2.5/weather",
                    params={'q': 'Moscow,RU', 'type': 'like', 'units': 'metric', 'lang': 'ru', 'APPID': APPID})
        data_temp = request_web.json()
        bot.send_message(message.chat.id, '\t\t\t' + str(data_temp['name'])+ '\n' +
                                          'Температура сейчас: ' + str(data_temp['main']['temp'] )+ '°C'+ '\n' +
                                          'Минимальная температура: ' + str(data_temp['main']['temp_min'] )+ '°C'+ '\n' +
                                          'Максимальная температура: ' + str(data_temp['main']['temp_max'] )+ '°C')
    
    elif message.text.strip() == 'Санкт-Петербург': 
        request_web = requests.get("http://api.openweathermap.org/data/2.5/weather",
                    params={'q': 'Saint Petersburg,RU', 'type': 'like', 'units': 'metric', 'lang': 'ru', 'APPID': APPID})
        data_temp = request_web.json()
        bot.send_message(message.chat.id, '\t\t\t' + str(data_temp['name'])+ '\n' +
                                          'Температура сейчас: ' + str(data_temp['main']['temp'] )+ '°C'+ '\n' +
                                          'Минимальная температура: ' + str(data_temp['main']['temp_min'] )+ '°C'+ '\n' +
                                          'Максимальная температура: ' + str(data_temp['main']['temp_max'] )+ '°C')

    elif message.text.strip() == 'Астрахань': 
        request_web = requests.get("http://api.openweathermap.org/data/2.5/weather",
                    params={'q': 'Astrakhan,RU', 'type': 'like', 'units': 'metric', 'lang': 'ru', 'APPID': APPID})
        data_temp = request_web.json()
        bot.send_message(message.chat.id, '\t\t\t' + str(data_temp['name'])+ '\n' +
                                          'Температура сейчас: ' + str(data_temp['main']['temp'] )+ '°C'+ '\n' +
                                          'Минимальная температура: ' + str(data_temp['main']['temp_min'] )+ '°C'+ '\n' +
                                          'Максимальная температура: ' + str(data_temp['main']['temp_max'] )+ '°C')

    elif message.text.strip() == 'Назад':
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton("Новый анекдот")
        item2=types.KeyboardButton("Погода")
        markup.add(item1, item2)
        bot.send_message(message.chat.id, 'Нажми: ',  reply_markup=markup)


bot.polling(none_stop=True, interval=0)
 
