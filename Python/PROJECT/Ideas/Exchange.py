#?access_key=fffc5f34895f627679275099f64cf727
import requests
import json

def Exchange(first, second):

    payload = {'base': first, 'symbols': second}
    response = requests.get('https://api.exchangeratesapi.io/latest', params=payload)

    #Json DATA to Python DATA
    Json = response.text
    Python = json.loads(Json)

    RATES = Python

    Convert_Rate = RATES['rates'][second]
    print(Convert_Rate)

Exchange('EUR', 'JPY')
