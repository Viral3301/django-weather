from django.shortcuts import render
from django.views.generic import TemplateView
import requests
import datetime
# Create your views here.

def index(request):

    if 'city' in request.POST:
        city = request.POST['city']
    else:
        city = "Amsterdam"

    appid = '21dfd30c6cbab790abf114f7ca12e577'
    URL = 'http://api.openweathermap.org/data/2.5/forecast'
    PARAMS = {'q' : city,'appid': appid,'lang' : 'ru','units' : 'metric'}
    city_json = requests.get(url=URL,params=PARAMS).json()
    current_hour_from_json = datetime.datetime.strptime(city_json['list'][0]['dt_txt'],'%Y-%m-%d %H:%M:%S').hour
    weather = {
        'city' : city_json['city']['name'],
        'temperature' : int(city_json['list'][0]['main']['temp']),
        'feels_like' : int(city_json['list'][0]['main']['feels_like']),
        'description' : city_json['list'][0]['weather'][0]['description'],
        'icon' : city_json['list'][0]['weather'][0]['icon'],
        'tomorrow_temperature' : int(city_json['list'][int(8/2 + (8 - current_hour_from_json/3))]['main']['temp']),
        'tomorrow_icon' : city_json['list'][int(8/2 + (8 - current_hour_from_json/3))]['weather'][0]['icon'],
        'day_after_tomorrow_temperature' : int(city_json['list'][int( 8 + (8/2 + (8 - current_hour_from_json/3)))]['main']['temp']),
        'day_after_tomorrow_icon' : city_json['list'][int( 8 + (8/2 + (8 - current_hour_from_json/3)))]['weather'][0]['icon'],
    }

    return render(request,'base.html',context={'weather': weather})
