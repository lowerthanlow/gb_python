FILENAME = 'bakery.csv'

sale = input()

with open('bakery.csv', 'a', encoding='utf-8') as file:
  file.write(f'{sale}\n')


