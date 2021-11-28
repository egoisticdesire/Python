from itertools import cycle
from time import sleep


class TrafficLight:
    def __init__(self):
        self.__colors = ('красный', 'желтый', 'зеленый')

    @staticmethod
    def __seconds_count(sec):
        for x in reversed(range(1, sec + 1)):
            print(f'Осталось {x} сек')
            sleep(1)

    def running(self):
        color = cycle(self.__colors)
        while color:
            print(f'Загорелся {next(color)} - стой!')
            self.__seconds_count(7)
            print(f'Загорелся {next(color)} - ожидай...')
            self.__seconds_count(2)
            print(f'Загорелся {next(color)} - иди!')
            self.__seconds_count(5)


traffic_light = TrafficLight()
traffic_light.running()
