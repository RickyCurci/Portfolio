#!/usr/bin/python
import requests;
import time;
import json;


city = 'Pietra Ligure'
def get_req(city):

    response = requests.get('https://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=921022f05a78a4b5bfe92af06dcd11d5')

    Json = response.text
    Python = json.loads(Json)

    Data = Python
    clock = time.asctime(time.localtime(time.time()))

    Celsius = int(Data['main']['temp'] - 273.15)
    Fahrenheit = int(Celsius * 1.8000 + 32.0000)


    Pressure = int(Data['main']['pressure'])
    Humidity = int(Data['main']['humidity'])
    Wind = int(Data['wind']['speed'])
    def Interface():

        print(' ')
        print(city+" "+Data['sys']['country'])
        print(clock)

        print(' ')

        print(Data['weather'][0]['description'])
        print(' ')

        print('TEMPERATURE            ||      PRESSURE: '+str(Pressure)+' mbar')
        print('                       ||      HUMIDITY: '+str(Humidity)+' %')
        print(str(Celsius)+" C  |  "+str(Fahrenheit)+' F          ||      WIND: '+str(Wind)+' KM/H')
        print(' ')
    Interface()

get_req(city)
