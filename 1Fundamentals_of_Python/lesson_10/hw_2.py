from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def coat(self):
        pass

    @abstractmethod
    def costume(self):
        pass


class MyClothes(Clothes):
    def __init__(self, size, growth):
        self.coat_size = round(size / 6.5 + 0.5, 2)
        self.costume_growth = round(growth * 2 + 0.3, 2)

    @property
    def coat(self):
        return self.coat_size

    @property
    def costume(self):
        return self.costume_growth


my_clothes = MyClothes(50, 180)
print(my_clothes.coat_size)
print(my_clothes.costume_growth)
