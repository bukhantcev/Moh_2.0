from bs4 import BeautifulSoup as BS
import urllib.request
import ssl
from datetime import datetime
ssl._create_default_https_context = ssl._create_unverified_context

def pars_me(url, element, name):
    f = urllib.request.urlopen(url).read()
    soup = BS(f, 'html.parser')
    divs = soup.find_all(element)
    result_list = []
    for div in divs:
        result = ''
        if name in str(div.get('class')):
            for i in str(div.text):
                if i.isalpha() or i == ' ' or i.isdigit() or i == '.' or i == ',' or i == ':':
                    result += i
            result_list.append(result)

    return result_list





def create_event(url):


    element_div = 'div'
    element_h3 = 'h3'
    name_title = 'с-playbill--item--content-title'
    name_date_day = 'с-playbill--item--date-dayNumber'
    name_date_month = 'с-playbill--item--date-content-month'
    name_date_year = 'с-playbill--item--date-content-year'
    name_time = 'с-playbill--item--date-content-time'
    name_location = 'с-playbill--item--content-scene'
    name_title_list = pars_me(url, element_h3, name_title)
    name_date_day_list = pars_me(url, element_div, name_date_day)
    name_date_month_list = []
    name_location_list = pars_me(url, element_div, name_location)
    dict_month = {'января':1, 'февраля':2, 'марта':3, 'апреля':4, 'мая':5, 'июня':6, 'июля':7, 'августа':8, 'сентября':9, 'октября':10, 'ноября':11, 'декабря':12}
    for i in pars_me(url, element_div, name_date_month):
        if i in dict_month:
            name_date_month_list.append(dict_month[i])

    name_date_year_list = pars_me(url, element_div, name_date_year)
    name_time_list = pars_me(url, element_div, name_time)
    event_list = []
    for i in range(len(name_date_day_list)):
        event_list.append({'date': datetime.strptime(f'{name_date_year_list[i]}-{name_date_month_list[i]}-{name_date_day_list[i]} {name_time_list[i]}:00', '%Y-%m-%d %H:%M:%S'), 'name':name_title_list[i], 'location':name_location_list[i].strip()})
    return event_list


