import schedule
from bot.bot import Bot
from bot.handler import MessageHandler
import covid
import processing
import time
import os
import pickle
import random 
NFILMSALNOE = 0
NFILMSFAMILY = 3
NEXPERIMENTS = 0
NMEMES = 0
TOKEN = "001.3273522775.2055291012:752357883"
bot = Bot(token=TOKEN)

def send_graph(country, uid):
    print("Here at send graph..")
    check_file = os.path.exists(country + 'plot.png')
    create_new = True
    if check_file:
        tcreate = os.path.getmtime(country + 'plot.png')
        tnow = time.time()
        if (tnow - tcreate) / 3600 >= 1:
            pass
        else:
            create_new = False
    if create_new:
        processing.plot(country)
    
    with open(country+'plot.png', "rb") as file:
        bot.send_file(chat_id=uid, file=file)
    
    
    # bot.send_file(chat_id=uid, file=country+'hist.jpg')    
    print("Finished send grpah.")
    
    
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
А еще мы можем подсказать, как скоротать время: /whattodo
Удачи и не болейте!"""

    
    def message_cb(bot, event):
        
        msg = event.text 
        if msg == '/start':
            s = set()
            bot.send_text(chat_id=event.from_chat, text=hello_msg)
            if os.path.exists("IDs.pckl"):
                with open("IDs.pckl", "rb") as f:
                    s = pickle.load(f)
            s.add(event.from_chat)
            with open("IDs1.pckl", "wb") as f:
                pickle.dump(s, file=f)
            os.rename("IDs1.pckl", "IDs.pckl")

        elif msg == '/Russia':
            bot.send_text(chat_id=event.from_chat, text=GetInfo('Russia'))
            send_graph("Russia", event.from_chat)

        elif msg == "/whattodo":
            inf = """
Во время самоизоляции очень важно найти занятие по душе,
и у нас есть несколько вариантов чтоб вам помочь:)
Вы можете посмотреть подборку семейных фильмов и сериалов: /familyfilms
И фильмов для тех, кто остался наедине с собой: /alonefilms
Ну а если помимо свободного времени у вас
есть научное любопытство, вы можете посмотреть 
подборку интересных опытов по физике: /experiments
Кстати, лайфхак: вы всегда можете поиграть в настолки,
даже если вы далеко от друзей, многие популярные игры 
имеют онлайн версии, например, монополия. Проверяли, затягивает:))
"""
            bot.send_text(chat_id=event.from_chat, text=inf)
        
        elif msg == "/familyfilms":
            films = []
            with open("./familyfilms" + str(random.randrange(1, NFILMSFAMILY + 1)) + ".txt", 'r') as f:
                films = f.read().split('\n')
            inf = "Вот список фильмов, которые мы рекомендуем посмотреть:\n" + '\n'.join(films)
            bot.send_text(chat_id=event.from_chat, text=inf)

        elif msg == "/alonefilms":
            films = []
            with open("./alonefilms" + str(random.randrange(1, NFILMSALNOE + 1)) + ".txt", 'r') as f:
                films = f.read().split('\n')
            inf = "Вот список фильмов, которые мы рекомендуем посмотреть:\n" + '\n'.join(films)
            bot.send_text(chat_id=event.from_chat, text=inf)

        elif msg == "/experiments":
            exp = ""
            with open("./experiments" + str(random.randrange(1, NEXPERIMENTS + 1)) + '.txt', 'r') as f:
                exp = f.read()
            bot.send_text(chat_id=event.from_chat, text=exp)
             
        else:
            inf = GetInfo(msg)
            print(inf)
            if inf == 'empty':
                bot.send_text(chat_id=event.from_chat, text="Простите, такого я не понимаю:(")
            else:
                bot.send_text(chat_id=event.from_chat, text=inf)
                
                send_graph(msg, event.from_chat)


    bot.dispatcher.add_handler(MessageHandler(callback=message_cb))
    bot.start_polling()
    bot.idle()