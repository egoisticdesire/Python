class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def mass_calculation(self, weight, thickness):
        return f'{self._length} м * {self._width} м * {weight} кг * {thickness} см = ' \
               f'{int(self._length * self._width * weight * thickness / 1000)} т'


road_section_1 = Road(5000, 20)
print(road_section_1.mass_calculation(25, 5))

