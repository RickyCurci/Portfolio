#!/usr/bin/python
#?access_key=fffc5f34895f627679275099f64cf727
import requests
import json





def Exchange():

    VALUE = []

    first = 'EUR'
    second = 'USD'


    payload = {'base': first, 'symbols': second}
    response = requests.get('https://api.exchangeratesapi.io/latest', params=payload)

    #Json DATA to Python DATA
    Json = response.text
    Python = json.loads(Json)

    #Value Conversion
    RATES = Python
    Convert_Rate = RATES['rates'][second]

    Quantity = int(input('QUANTITY: '))
    Convert_Rate = Convert_Rate * Quantity
    print(str(Quantity)+ ' ' + first + ' in ' + second + ' is rate ' + str(Convert_Rate))

Exchange()
