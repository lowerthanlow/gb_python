class Road:
  def __init__(self, length, width):
    self._length = length
    self._width = width


  def calc(self, mass, thickness):
     return ((self._length * self._width * mass * thickness) // 1000)


road = Road(length=20, width=5000)
print(f'{road.calc(25, 5)} т')

   