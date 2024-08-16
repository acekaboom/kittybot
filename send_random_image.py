import requests
from telebot import TeleBot

bot = TeleBot(token=TOKEN)

URL = 'https://api.thecatapi.com/v1/images/search'
response = requests.get(URL).json()
kitten_photo = response[0].get('url')

chat_id = ACCOUNT_SID
text = 'Вам телеграмма!'

bot.send_message(chat_id, text)
bot.send_photo(chat_id, kitten_photo)
