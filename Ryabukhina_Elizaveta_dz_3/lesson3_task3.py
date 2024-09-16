
dictionary_names = {}

def thesaurus(*names):
  for name in names:
    letters = name[0]
      
    if letters not in dictionary_names:
      dictionary_names[letters] = []
    dictionary_names[letters].append(name)
  return dictionary_names

print(thesaurus("Иван", "Мария", "Петр", "Илья"))
