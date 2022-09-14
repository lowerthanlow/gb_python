import random
import numpy as np


class Matrix:
  def __init__(self, matrix):
    self.matrix = matrix 

  def __str__(self):
    return f'{np.array(self.matrix)}'


  def __add__(self, other):
    return (np.add(self.matrix, other.matrix))
    

def fill():
    return [[random.randint(-10, 10) for i in range(3)]
            for i in range(3)]    



matrix_1 = Matrix(fill())
print(matrix_1)
print()

matrix_2 = Matrix(fill())
print(matrix_2)

print()
print(matrix_1 + matrix_2)