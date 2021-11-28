class Worker:
    def __init__(self, income):
        self.name = input('Ваше имя: ')
        self.surname = input('Ваша фамилия: ')
        self.position = input('Ваша должность: ')
        self._income_wage = income['wage']
        self._income_bonus = income['bonus']


class Position(Worker):
    def get_full_name(self):
        return f'\nСотрудник: {self.name} {self.surname}\nЗанимаемая должность: {self.position}'

    def get_total_income(self):
        return f'\nСотрудник: {self.name} {self.surname}\nВ этом месяце Вы заработали ' \
               f'(оклад: {self._income_wage} тыс. руб. и премия: {self._income_bonus} тыс. руб.): ' \
               f'{self._income_wage + self._income_bonus} тыс. руб.'


worker = Position({'wage': 30, 'bonus': 10})
print(worker.get_full_name())
print(worker.get_total_income())
