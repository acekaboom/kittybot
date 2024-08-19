import requests
from telebot import TeleBot
import os
from dotenv import load_dotenv

load_dotenv()
# Теперь переменная TOKEN, описанная в файле .env,
# доступна в пространстве переменных окружения.

TOKEN = os.getenv('TOKEN')
ACCOUNT_SID = os.getenv('ACCOUNT_SID')

bot = TeleBot(token=TOKEN)

URL = 'https://api.thecatapi.com/v1/images/search'
response = requests.get(URL).json()
kitten_photo = response[0].get('url')

chat_id = ACCOUNT_SID
text = 'Вам телеграмма!'

bot.send_message(chat_id, text)
bot.send_photo(chat_id, kitten_photo)
