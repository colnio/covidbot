import covid

cov = covid.Covid()

def GetInfo(country='total'):
    global cov 
    list_countries = [i['name'] for i in list(cov.list_countries())]
    if country == 'total':
        message = """
        Всего подтвержденных случаев: %s
        Выздоровевших: %s
        Число смертей: %s
        """ % (cov.get_total_confirmed_cases(), cov.get_total_recovered(), cov.get_total_deaths())
    
    elif country in  list_countries:
        status = cov.get_status_by_country_name(country)
        message = """
        Всего подтвержденных случаев: %s
        Выздоровевших: %s
        Число смертей: %s
        """ % (status['confirmed'], status['recovered'], status['deaths'])
    else:
        message = 'empty'
    return message

if __name__=="__main__":
    while 1:
        print(GetInfo(input()))