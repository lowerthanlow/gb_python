from itertools import zip_longest

tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей', 
    'Дмитрий', 'Борис', 'Елена'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А', 
]

if len(tutors) > len(klasses):
  print(*(tuple(x) for x in zip_longest(tutors, klasses, fillvalue='None')))  
else:
  print(*(tuple(x) for x in zip(tutors, klasses))) 
  