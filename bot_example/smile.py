from distutils.cmd import Command
import telebot
import PIL
from PIL import Image
from requests import get



API_KEY = str(open('/home/nelud/KEY/API_KEY_BOT.txt', 'r').read()).strip()
bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,  "Пришли мне смайлик")

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'нам первый смайлик':
        img = open('Смайлики и люди 1.png', 'rb')
        
        bot.send_document(message.chat.id, img) 
    elif message.text.lower() == 'наш второй смайлик':
        img = open('Смайлики и люди 2.png', 'rb')
        bot.send_document(message.chat.id, img)    
   
    else:
        bot.send_message(message.chat.id, 'Сасай кудасай')

bot.polling()
