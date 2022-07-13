from select import POLLIN
import requests
from bs4 import BeautifulSoup as bs
import random
import telebot





URL = 'https://www.anekdot.ru/last/burning/'
API_KEY = str(open('/home/nelud/KEY/API_KEY_BOT.txt', 'r').read()).strip()

def parser(url):
    request_web = requests.get(url)
    # print(request_web.status_code)
    # print(request_web.text)
    soup = bs(request_web.text, 'html.parser')
    anekdots = soup.find_all('div', class_='text')
    return [item.text for item in anekdots]


list_of_jokes = parser(URL)
random.shuffle(list_of_jokes)

bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands=['начать'])
def hello(message):
    bot.send_message(message.chat.id, 'Привет! Введите любую цифру: ')

@bot.message_handler(content_types=['text'])
def jokes(message):
    if message.text.lower() in '123456789':
        bot.send_message(message.chat.id, list_of_jokes[0]) 
        del list_of_jokes[0]
    else:
        bot.send_message(message.chat.id, 'Введите любую цифру: ')

bot.polling()

