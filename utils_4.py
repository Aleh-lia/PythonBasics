import requests
from decimal import *
from datetime import datetime

getcontext().prec = 10


def currency_rates(val, quantity = 1):
    val = val.upper()
    address = 'http://www.cbr.ru/scripts/XML_daily.asp'
    response = requests.get(address).text


    if val not in response:
        return None

    rub = response[response.find('<Value>', response.find(val)) + 7:response.find('</Value>', response.find(val))]
    date_crude = response[response.find('Date="') + 6:response.find('"', response.find('Date="') + 6)].split('.')
    day, month, year = map(int, date_crude)
    date = datetime(day=day, month=month, year=year)
    return f" {quantity} {val} = {Decimal(rub.replace(',', '.')) * quantity} RUB на {datetime.strftime(date, '%d.%m.%Y')}"


if __name__ == '__main__':
    import sys
    print(sys.argv)