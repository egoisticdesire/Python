from datetime import date

from decimal import *

from requests import get


def currency_rates(value):
    value = value.upper()
    response = get('http://www.cbr.ru/scripts/XML_daily.asp').text

    if value not in response:
        return None

    currency = response[
               response.find('<Value>', response.find(value)) + 7:response.find('</Value>', response.find(value))]
    currency_date = response[response.find('Date="') + 6:response.find('"', response.find('Date="') + 6)].split('.')
    day, month, year = map(int, currency_date)
    return f'Стоимость 1 {value} составляет {Decimal(currency.replace(",", "."))}, ' \
           f'по состоянию на {date(day=day, month=month, year=year)}'


getcontext().prec = 4

if __name__ == '__main__':
    print(currency_rates('USD'))
    print(currency_rates('eur'))
