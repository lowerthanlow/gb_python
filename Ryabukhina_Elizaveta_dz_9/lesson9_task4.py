class Car:
  def __init__(self, speed, color, name):
    self.speed = speed
    self.color = color 
    self.name = name  
    self.is_police = False

  def go (self):
    return f'{self.name} went'


  def stop(self):
    return f'{self.name} stopped'

  
  def turn(self, direction):
    if direction == 'right':
      return f'{self.name} turned right'
    elif direction == 'left':
      return f'{self.name} turned left'


  def show_speed(self):
    return f'{self.speed} km/h'


class TownCar(Car):
  def show_speed(self):
    if self.speed > 60:
      return f'OVERSPEED! {self.name} was driving {self.speed} km/h'
    return f'{self.speed} km/h'  



class SportCar(Car):
  def __init__(self, speed, color, name):
    super().__init__(speed, color, name)


class WorkCar(Car):
  def show_speed(self):
    if self.speed > 40:
      return f'OVERSPEED! {self.name} was driving {self.speed} km/h'
    return f'{self.speed} km/h' 


class PoliceCar(Car):
  def __init__(self, speed, color, name):
    super().__init__(speed, color, name)
    self.is_police = True


car = WorkCar(100, 'white', 'lada')
print(car.go())
print(car.show_speed())
print(car.turn('left'))
print(car.turn('right'))
print(car.stop())
