import random

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]



def get_jokes(n):
    """Функция возвращает n шуток, сформированных из трех случайных слов, взятых из трёх списков (по одному из каждого)"""

    for i in range(n):
      random_el = random.choice(nouns)
      random_el1 = random.choice(adverbs)
      random_el2 = random.choice(adjectives)

      joke = (' '.join([random_el, random_el1, random_el2]))
      
      print(joke)

get_jokes(random.randint(1,5))
    

    




















