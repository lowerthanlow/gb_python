import requests
import json
from datetime import datetime

URL = 'https://www.cbr-xml-daily.ru/daily_json.js'

def currency_rates(currency_code):
  response = requests.get(URL)
  dict = json.loads(response.text)

  currency_code = currency_code.upper()
  value_currency = dict['Valute'][currency_code]['Value']
  
  date = datetime.fromisoformat(dict['Date'])
  date = date.strftime('%d/%m/%Y')
  
  res = f'{value_currency} {date}'
  print(res)

if __name__ == '__main__':
 currency_rates('usd')
 currency_rates('eur')