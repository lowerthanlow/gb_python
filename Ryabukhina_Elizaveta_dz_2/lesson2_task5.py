put = [57.8, 46.51, 97, 87.9, 18, 47.13, 89.5, 75, 65.9, 10]

put_id = id(put)
print('id до сортировки = ', put_id)
print()

put.sort()

for i in put:
  r = int(i)
  kk = (i - int(i)) * 100
  kk = str(round(kk)).zfill(2)
  print(r, 'руб' , kk, 'коп')

print()
put_id = id(put)
print('id после сортировки = ', put_id)
print()

put2 = [57.8, 46.51, 97, 87.9, 18, 47.13, 89.5, 75, 65.9, 10]


put2.sort(reverse=True)

for i in put2:
  r = int(i)
  kk = (i - int(i)) * 100
  kk = str(round(kk)).zfill(2)
  print(r, 'руб' , kk, 'коп')

print()  
print('цена пяти самых дорогих товаров = ', str(put2[0:4]).strip('[]'))