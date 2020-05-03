import threading
import urllib.request
import schedule
import time
import ssl
import os


i = 0
if i == 0:
    print('Beginning file download with urllib2...')
    ssl._create_default_https_context = ssl._create_unverified_context
    url = 'https://github.com/owid/covid-19-data/raw/master/public/data/owid-covid-data.xlsx'
    urllib.request.urlretrieve(url, 'covid_data1.xlsx')

i = 1



def downloading():
    print('Beginning file download with urllib2...')
    url = 'https://github.com/owid/covid-19-data/raw/master/public/data/owid-covid-data.xlsx'
    ssl._create_default_https_context = ssl._create_unverified_context
    urllib.request.urlretrieve(url, 'covid_data_1.xlsx')
    print('downloaded')
    check_file = os.path.exists('сovid_data.xlsx')
    print('check done ', check_file)
    if check_file == True:
    path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'covid_data.xlsx')
    os.remove(path)
    else: 
        pass
    os.rename('covid_data_1.xlsx', 'covid_data.xlsx')

   

# def run_threaded(downloading):
#     job_thread = threading.Thread(target=downloading, daemon = True)
#     job_thread.start()

schedule.every.day.at('8:00').do(downloading)
schedule.every.day.at('9:00').do(downloading)
schedule.every.day.at('10:00').do(downloading)
schedule.every.day.at('12:00').do(downloading)
schedule.every.day.at('13:00').do(downloading)
schedule.every.day.at('14:00').do(downloading)
schedule.every.day.at('15:00').do(downloading)
schedule.every.day.at('16:00').do(downloading)
schedule.every.day.at('17:00').do(downloading)
schedule.every.day.at('18:00').do(downloading)
schedule.every.day.at('19:00').do(downloading)
schedule.every.day.at('20:00').do(downloading)
schedule.every.day.at('21:00').do(downloading)
schedule.every.day.at('22:00').do(downloading)
schedule.every.day.at('23:00').do(downloading)
schedule.every.day.at('00:00').do(downloading)

while True:
    schedule.run_pending()
    time.sleep(1)