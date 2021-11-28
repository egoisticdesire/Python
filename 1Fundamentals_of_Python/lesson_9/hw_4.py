class Car:
    def __init__(self, name, color, speed, is_police=False):
        self._name = name
        self._color = color
        self._speed = speed
        self._is_police = is_police

    def go(self):
        print(f'\nАвтомобиль {self._name} начал движение и набрал скорость {self._speed} км/ч')

    def stop(self):
        print(f'Автомобиль {self._name} остановился')

    def turn(self, direction):
        print(f'Автомобиль {self._name} повернул {direction}')

    def show_speed(self):
        print(f'Текущая скорость автомобиля {self._name}: {self._speed} км/ч')


class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self._speed > 60:
            print('\tНеобходимо снизить скорость до 60 км/ч!')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if self._speed > 40:
            print('\tНеобходимо снизить скорость до 40 км/ч!')


class PoliceCar(Car):
    pass


town_car = TownCar('Renault', 'white', 100)
sport_car = SportCar('Ferrari', 'yellow', 200)
work_car = WorkCar('Lada', 'blue', 50)
police_car = PoliceCar('Toyota', 'black', 150, is_police=True)

town_car.go()
town_car.turn('налево')
town_car.show_speed()
town_car.stop()

sport_car.go()
sport_car.turn('направо')
sport_car.show_speed()
sport_car.stop()

work_car.go()
work_car.turn('прямиком в ад')
work_car.show_speed()
work_car.stop()

police_car.go()
police_car.turn('за нарушителем')
police_car.show_speed()
police_car.stop()
