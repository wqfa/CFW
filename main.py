try:
	import telebot
	import requests
	import os
	from os import system
except:
	system('pip install pyTelegramBotAPI==3.7.7')
	system('pip install mechanize')
	system('pip install PyTelegramBotApi')
	system('pip install telebot')
	system('pip install requests')
#شغل الاداة وراها حط توكنك وروح للبوت دوس /start ويشتغل وياك
token="5393921528:AAEMpK64XMx3ALMeNIG82zjD2AhCjzMXowM"
bot=telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def start(message):
	bot.reply_to(message,'هـلا بـيـك بـوت اسـتـخـراج مـعـلومـات انـسـتـكـرام كـامـلـه 🤖')
	bot.send_message(message.chat.id,'ارسـل يـوزر الـحسـاب الـمـطـلوب 🔱')
	
	@bot.message_handler(func=lambda message:True)
	def yahya(message):
		user=(message.text)

		url=f'https://i.instagram.com/api/v1/users/web_profile_info/?username={user}'
		head={'user-agent':'Mozilla/5.0 (Linux; Android 11; SM-A205F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.40 Mobile Safari/537.36',
'viewport-width':'412',
'x-asbd-id':'198387',
'x-ig-app-id':'1217981644879628',
'x-ig-www-claim':'hmac.AR1GMxGxYNiyJ_Qr59WPgznfqJKtnAogUcpBr_5hDMSoxwjz'}
		try:
			req=requests.get(url,headers=head).json()['data']['user']
			id=req['id']
			img=req["profile_pic_url_hd"]
			name=req['full_name']
			fol=req['edge_followed_by']['count']
			fols=req['edge_follow']['count']
			re = requests.get(f"https://o7aa.pythonanywhere.com/?id={id}")
			rr=re.json()
			r=rr['date']
			
			
			bio=req['edge_owner_to_timeline_media']['count']
			ii=req['is_private']
			ya=f'⌁︙اسم المستخدم:{name}\n⌁︙عدد المتابعين: {fol}\n⌁︙عدد الذين يتابعهم: {fols}\n⌁︙البايو: {bio}\n⌁︙التحقق: {ii}\n⌁︙التاريخ: :{r}\n⌁︙مطور البوت🤵🏻🤟🏻: @C15CS'
		
			bot.send_photo(message.chat.id,img,ya)
		except:
			bot.send_message(message.chat.id,'عـذرا الـيـوزر مـتـبـنـد او الـحـسـاب مـوقـف 😔')
	

bot.polling(True)
	