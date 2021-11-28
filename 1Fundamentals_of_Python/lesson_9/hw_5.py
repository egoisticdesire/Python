class Stationery:
    def __init__(self, title=None):
        self._title = title

    def draw(self):
        print(f'Запуск отрисовки!')


class Pen(Stationery):
    def draw(self):
        print(f'Запуск отрисовки: {self._title}')


class Pencil(Stationery):
    def draw(self):
        print(f'Запуск отрисовки: {self._title}')


class Handle(Stationery):
    def draw(self):
        print(f'Запуск отрисовки: {self._title}')


stationery = Stationery()
stationery.draw()
pen = Pen('Ручка')
pen.draw()
pencil = Pencil('Карандаш')
pencil.draw()
handle = Handle('Маркер')
handle.draw()
