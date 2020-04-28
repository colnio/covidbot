import schedule
from bot.bot import Bot
from bot.handler import MessageHandler
import covid

cov = covid.Covid()

def GetInfo(country='/total'):
    global cov 
    list_countries = [i['name'] for i in list(cov.list_countries())]
    if country == '/total':
        message = """
Всего подтвержденных случаев: %s
Выздоровевших: %s
Число смертей: %s
""" % (cov.get_total_confirmed_cases(), cov.get_total_recovered(), cov.get_total_deaths())
    
    elif country in  list_countries:
        print("country info")
        status = cov.get_status_by_country_name(country)
        message = """
Всего подтвержденных случаев: %s
Выздоровевших: %s
Число смертей: %s
        """ % (status['confirmed'], status['recovered'], status['deaths'])
    else:
        message = 'empty'
    print("GetInfo")
    return message

hello_msg = """
Привет! Я могу сообщать тебе последние новости о коронавирусе.
Пока я умею немного, но мы над этим работаем.
Чтобы посмотреть общую статистику: /total
Чтобы посмотреть статистику по России: /Russia
Также ты можешь посмотреть информацию по любой стране,
просто написав ее название (пока что только на английском).
Удачи и не болейте!"""

TOKEN = "001.3273522775.2055291012:752357883"
bot = Bot(token=TOKEN)

def message_cb(bot, event):
    msg = event.text 
    if msg == '/start':
        bot.send_text(chat_id=event.from_chat, text=hello_msg)
    elif msg == '/Russia':
        bot.send_text(chat_id=event.from_chat, text=GetInfo('Russia'))
    else:
        inf = GetInfo(msg)
        print(inf)
        if inf == 'empty':
            bot.send_text(chat_id=event.from_chat, text="Простите, такого я не понимаю:(")
        else:
            bot.send_text(chat_id=event.from_chat, text=inf)
    # bot.send_text(chat_id=event.from_chat, text=event.text)

bot.dispatcher.add_handler(MessageHandler(callback=message_cb))
bot.start_polling()
bot.idle()