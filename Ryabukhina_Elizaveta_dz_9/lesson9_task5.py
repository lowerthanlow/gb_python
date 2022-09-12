class Stationery:
  def __init__(self, title):
    self.title = title

  def draw(self):
    print('Запуск отрисовки')

class Pen(Stationery):
  def __init__(self, title):
    super().__init__(title)

  def draw(self):
    print('Пишем ручкой')


class Pencil(Stationery):
  def __init__(self, title):
    super().__init__(title)

  def draw(self):
    print('Рисуем карандашом')


class Handle(Stationery):
  def __init__(self, title):
    super().__init__(title)

  def draw(self):
    print("Выделяем заголовки")


a = Stationery('')
a.draw()

pen = Pen('Ручка')
pen.draw()

pencil = Pencil('Карандаш')
pencil.draw()

handle = Handle('Маркер')
handle.draw()