import schedule
from bot.bot import Bot
from bot.handler import MessageHandler
import covid
import processing
import time
import os

TOKEN = "001.3273522775.2055291012:752357883"
bot = Bot(token=TOKEN)

def send_graph(country, uid):
    
    check_file = os.path.exists(country + 'plot.jpg')
    create_new = True
    if check_file:
        tcreate = os.path.getmtime(country + 'plot.jpg')
        tnow = time.time()
        if (tnow - tcreate) / 3600 >= 1:
            pass
        else:
            create_new = False
    if create_new:
        processing.plot(country)
    bot.send_file(chat_id=uid, file=country+'plot.jpg')
    bot.send_file(chat_id=uid, file=country+'hist.jpg')    
    




    
def listen():

    

    cov = covid.Covid()

    # GetInfo получает информацию о количестве заболевших,
    # Выздоровевших и умерших по данной стране,
    # Пользуясь данными университета хопкинса 
    # через covid api

    def GetInfo(country='/total'):
        list_countries = [i['name'] for i in list(cov.list_countries())]
        if country == '/total':
            message = """
Всего подтвержденных случаев: %s
Выздоровевших: %s
Число смертей: %s
    """ % (cov.get_total_confirmed_cases(), cov.get_total_recovered(), cov.get_total_deaths())
            return message
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

    

    def message_cb(bot, event):
        msg = event.text 
        if msg == '/start':
            bot.send_text(chat_id=event.from_chat, text=hello_msg)
        elif msg == '/Russia':
            bot.send_text(chat_id=event.from_chat, text=GetInfo('Russia'))
            # TODO: place the plotting func here
            # bot.send_file(chat_id=event.from_chat, file="Russia.jpg")
        else:
            inf = GetInfo(msg)
            print(inf)
            if inf == 'empty':
                bot.send_text(chat_id=event.from_chat, text="Простите, такого я не понимаю:(")
            else:
                bot.send_text(chat_id=event.from_chat, text=inf)
                # TODO: place the plotting func here
                # bot.send_file(chat_id=event.from_chat, file=msg+".jpg")


    bot.dispatcher.add_handler(MessageHandler(callback=message_cb))
    bot.start_polling()
    bot.idle()