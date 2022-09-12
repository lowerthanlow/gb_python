import time 


class TrafficLight:
  def __init__(self, color = 'red'):
    self.__color = color


  def running(self):
    for _ in range(10): 
      if self.__color == 'red':
       print(self.__color)
       self.__color = 'yellow'
       time.sleep(7)
      elif self.__color == 'yellow':
        print(self.__color)
        self.__color = 'green'
        time.sleep(2)
      elif self.__color == 'green':
        print(self.__color)
        self.__color = 'red'
        time.sleep(5)


traffic = TrafficLight()
traffic.running()