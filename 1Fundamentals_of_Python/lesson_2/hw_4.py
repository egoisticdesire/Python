corrupted_data = ['инженер-конструктор Игорь',
                  'главный бухгалтер МАРИНА',
                  'токарь высшего разряда нИКОЛАй',
                  'директор аэлита']


for element in corrupted_data:
    print(f'Привет, {element.split()[-1].title()}!')
