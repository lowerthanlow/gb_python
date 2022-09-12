class Worker:  
  def __init__(self, name, surname, position, wage, bonus = 0):
    self.name = name  
    self.surname = surname
    self.position = position
    self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
  def __init__(self, name, surname, position, wage, bonus):
      super().__init__(name, surname, position, wage, bonus)
    

  def get_full_name(self):
    return f'{self.surname} {self.name}'


  def get_total_income(self):
    return self._income['wage'] + self._income['bonus']

  
mike = Position("Михаил", "Иванов", "Юрист", 200, 10)
print(mike.get_full_name())
print(mike.get_total_income())