for i in list(range(1,101)):
  if i == 11 or i == 12 or i == 13 or i == 14:
    print(i, 'процентов')
  elif i % 10 == 1:
    print(i, 'процент')
  elif 1 < i % 10 < 5 :
    print(i, 'процента')
  else:
    print(i, 'процентов')