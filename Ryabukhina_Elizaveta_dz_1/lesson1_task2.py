numbers = list(range(1, 1000, 2))

for i in numbers:
  if sum(map(int, str(i**3))) % 7 == 0:
    print(i**3)


# К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
    
print()
print ('Задание b')
print()
    
numbers = list(range(1, 1000, 2))

for i in numbers:
  i = i +17
  if sum(map(int, str(i**3))) % 7 == 0:
     print(i**3)



