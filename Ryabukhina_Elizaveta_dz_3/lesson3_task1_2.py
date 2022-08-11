numbers = {
    "one": "один",
    "two": "два",
    "three": "три",
    "four": "четире",
    "five": "пять",
    "six": "шесть",
    "seven": "семь",
    "eight": "восемь",
    "nine": "девять",
    "zero": "ноль",
}

def num_translate_ad(number):
  for eng, rus in numbers.items():
    if eng == number:
      return rus
    elif eng.capitalize() == number:
      return rus.capitalize()

  
print(num_translate_ad(input()))

  