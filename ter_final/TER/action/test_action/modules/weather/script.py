## -*- coding: utf-8 -*-

import requests, time, datetime

API_KEY = '8ab70f719a364890fc01d44c6a5b4fc7'

def getTodayWeather(city):
    return requests.get('http://api.openweathermap.org/data/2.5/weather?APPID='+ API_KEY +'&units=metric&q='+ city).json()

def getTomorrowWeather(city, timestamp):
    resp = requests.get('http://api.openweathermap.org/data/2.5/forecast?APPID='+ API_KEY +'&units=metric&q='+ city).json()
    for w in resp['list']:
        if(int(w['dt'])>timestamp):
            return(w)

def getTodayWeatherResponse(city):
    weather = getTodayWeather(city)
    response = "Aujourd'hui à " + city + " la température est de " + str(round(weather['main']['temp'])).split('.')[0] + " degrés celsius " \
                "avec un  taux d'humidité de "+ str(weather['main']['humidity']) +" pourcent " \
                "et une pression atmosphérique de "+ str(weather['main']['pressure']) +" hectopascal."
    return response

def getTomorrowWeatherResponse(city, timestamp):
    weather = getTomorrowWeather(city, timestamp)
    response = "Demain à " + city + " la température prévu est de " + str(round(weather['main']['temp'])).split('.')[0] + " degrés celsius " \
                "avec un  taux d'humidité de "+ str(weather['main']['humidity']) +" pourcent " \
                "et une pression atmosphérique de "+ str(weather['main']['pressure']) +" hectopascal."
    return response


def getWeatherResponse(city, dt):

    print(city)
    print(dt)

    if(dt==''):
        return getTodayWeatherResponse(city)
    else:
        dt = dt.split('+')[0]
        t = time.mktime(datetime.datetime.strptime(dt, "%Y-%m-%dT%H:%M:%S").timetuple())
        day = int(dt.split('-')[2].split('T')[0])
        today = int(datetime.datetime.today().day)

        if(day==today):
            return getTodayWeatherResponse(city)
        elif(day==(today+1)):
            return getTomorrowWeatherResponse(city, t)
        else:
            return "Je ne connais pas la météo pour cette date."


#print(getWeatherResponse('Paris', '2018-06-13T12:00:00+04:00'))
#print(getWeatherResponse('Paris', ''))
