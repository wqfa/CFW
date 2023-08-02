import requests
import json
import telebot
from telebot import types

token = input(" ENTER YOUR TOKEN : ")
bot = telebot.TeleBot(token)
print('\033[2;32m\n \n        run')

headers = {
    'authority': 'randommer.io',
    'accept': '*/*',
    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://randommer.io',
    'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 12; M2004J19C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

@bot.message_handler(commands=["start"])
def welcome(message):
 
 my = types.InlineKeyboardButton(text='انضم بقناتي اولا',url="t.me/C35CS")
 xx = types.InlineKeyboardMarkup()
 xx.add(my)
 name = message.chat.first_name
 
 bot.reply_to(message,f'''اهلن {name}
انا بوت اعطيك فيز بلاش فقط قم بأرسال
ـ  /visa''',reply_markup=xx)

@bot.message_handler(commands=['visa'])
def visa(message):
     data = {
     'Type': 'visa',
     'X-Requested-With': 'XMLHttpRequest',}
     url = requests.post('https://randommer.io/Card',headers=headers, data=data)
     data = json.loads(url.content)
     card = data['cardNumber']
     name = data['fullName']
     cvv = data['cvv']
     pin = data['pin']
     type = data['type']
     date = data['date']
     text =f'Card Number: {card}\nFull Name: {name}\nCVV: {cvv}\nPin: {pin}\nExpiration Date: {date}\n \nTV : @DevEviI & @C35CS'
     bot.reply_to(message,text)


	    

bot.infinity_polling()



