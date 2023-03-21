from django.shortcuts import render
from django.views.generic import TemplateView
import requests
# Create your views here.

class HomeView(TemplateView):
    template_name = 'home.html'


    
        

    def get_context_data(self, **kwargs):
        
        appid = '21dfd30c6cbab790abf114f7ca12e577'
        URL = 'http://api.openweathermap.org/data/2.5/forecast'
        PARAMS = {'q' : 'Moscow','appid': appid,'lang' : 'ru','units' : 'metric'}
        city_json = requests.get(url=URL,params=PARAMS).json()

        weather = {
            'city' : city_json['city']['name'],
            'temperature' : int(city_json['list'][0]['main']['temp']),
            'feels_like' : int(city_json['list'][0]['main']['feels_like']),
            'description' : city_json['list'][0]['weather'][0]['description'],
            'icon' : city_json['list'][0]['weather'][0]['icon']
        }

        context = super().get_context_data(**kwargs)
        context['weather'] = weather
        return context