import threading
import urllib.request
import schedule
import time
import ssl
import os

def first_run():
    check_file = os.path.exists('covid_data1.csv')
    print('Beginning file download with urllib2...')
    url = 'https://github.com/owid/covid-19-data/raw/master/public/data/owid-covid-data.csv'
    ssl._create_default_https_context = ssl._create_unverified_context
    urllib.request.urlretrieve(url, 'covid_data1.csv')
    print('downloaded')
    check_file = os.path.exists('covid_data.csv')
    print('check done ', check_file)
    if check_file == True:
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'covid_data.csv')
        os.remove(path)
    else: 
        pass
    os.rename('covid_data1.csv', 'covid_data.csv')
    print('cool')

def update():

    # # check_file = os.path.exists('covid_data1.xlsx')
    # # if check_file == True:
    # #     path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'covid_data1.xlsx')
    # #     os.remove(path)
    # # else: 
    # #     pass
    # print('Beginning file download with urllib2...')
    # url = 'https://github.com/owid/covid-19-data/raw/master/public/data/owid-covid-data.xlsx'
    # ssl._create_default_https_context = ssl._create_unverified_context
    # urllib.request.urlretrieve(url, 'covid_data1.xlsx')
    # print('downloaded')
    # check_file = os.path.exists('covid_data.xlsx')
    # print('check done ', check_file)
    # if check_file == True:
    #     path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'covid_data.xlsx')
    #     os.remove(path)
    # else: 
    #     pass
    # os.rename('covid_data1.xlsx', 'covid_data.xlsx')
    # print('cool')





    def downloading():
        check_file = os.path.exists('сovid_data1.csv')
        if check_file == True:
            path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'covid_data1.csv')
            os.remove(path)
        else: 
            pass
        print('Beginning file download with urllib2...')
        url = 'https://github.com/owid/covid-19-data/raw/master/public/data/owid-covid-data.csv'
        ssl._create_default_https_context = ssl._create_unverified_context
        urllib.request.urlretrieve(url, 'covid_data1.csv')
        print('downloaded')
        check_file = os.path.exists('covid_data.csv')
        print('check done ', check_file)
        if check_file == True:
            path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'covid_data.csv')
            os.remove(path)
        else: 
            pass
        os.rename('covid_data1.xlsx', 'covid_data.csv')
        print('cool')



    schedule.every().day.at("08:00").do(downloading)
    schedule.every().day.at("09:00").do(downloading)
    schedule.every().day.at("10:00").do(downloading)
    schedule.every().day.at("11:00").do(downloading)
    schedule.every().day.at("12:00").do(downloading)
    schedule.every().day.at("13:00").do(downloading)
    schedule.every().day.at("14:00").do(downloading)
    schedule.every().day.at("15:00").do(downloading)
    schedule.every().day.at("16:00").do(downloading)
    schedule.every().day.at("17:00").do(downloading)
    schedule.every().day.at("18:00").do(downloading)
    schedule.every().day.at("19:00").do(downloading)
    schedule.every().day.at("20:00").do(downloading)
    schedule.every().day.at("21:00").do(downloading)
    schedule.every().day.at("22:00").do(downloading)
    schedule.every().day.at("23:00").do(downloading)
    schedule.every().day.at("00:00").do(downloading)


    while True:
        schedule.run_pending()
        time.sleep(1)
