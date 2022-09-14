class Cell:
  def __init__(self, number):
    self.number = int(number)


  def __str__(self):
    return f'{self.number}'  

  def __add__(self, other):
    return self.number + other.number

  def __sub__(self, other):
    if self.number < other.number:
      raise ValueError("разность меньше нуля") 
    return self.number - other.number

  def __mul__(self, other):
    return self.number * other.number

  def __floordiv__(self, other):
    return self.number // other.number


  def make_order(self, n):
    result = [i for i in range(self.number)]
    start = 0
    for i in result:
      start += 1
      print('*', end = '')      
      if start % n == 0:
        print (end = '\n')

   
cell_1 = Cell(22)
cell_2 = Cell(2)

print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 // cell_2)
print()
cell_1.make_order(6)
