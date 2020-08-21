#!/usr/bin/python
#?access_key=fffc5f34895f627679275099f64cf727
import requests
import json

first = 'EUR'
second = 'USD'



def Exchange(first, second):

    payload = {'base': first, 'symbols': second}
    response = requests.get('https://api.exchangeratesapi.io/latest', params=payload)

    #Json DATA to Python DATA
    Json = response.text
    Python = json.loads(Json)

    #Value Conversion
    RATES = Python
    Convert_Rate = RATES['rates'][second]

    Quantity = 900
    Convert_Rate = Convert_Rate * Quantity
    print(Convert_Rate)

Exchange(first, second)
