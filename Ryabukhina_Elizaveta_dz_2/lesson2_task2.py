put = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']


for i in range(len(put)):
    cell = put.pop(0)
    if  cell.startswith(('5', '1')):
        put.append('"' + str(cell).zfill(2) + '"')
    elif cell.startswith('+'):
        put.append('"' + str(cell).zfill(3) + '"')
    else:
        put.append(cell)
print(' '.join(put))











