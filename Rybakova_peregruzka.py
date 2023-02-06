class Airplane:
    def __init__(self, name: str, max_passenger: int, current_passenger: int):
        self.name = name
        self.max_passenger = max_passenger
        self.current_passenger = current_passenger

    # оператор "+"
    def __add__(self, other):
        return self.current_passenger + other

    # оператор "-"
    def __sub__(self, other):
        return self.current_passenger - other

    # оператор "+="
    def __iadd__(self, other):
        self.current_passenger += other
        return self

    # оператор "-="
    def __isub__(self, other):
        self.current_passenger -= other
        return self

    # оператор "+"
    def __radd__(self, other):
        return self.current_passenger + other

    # "=="
    def __eq__(self, other):
        if isinstance(other, Airplane):
            if self.name == other.name:
                return True
            else:
                return False
        else:
            return 'Неверный выбор операндов.'

    # "<"
    def __lt__(self, other):
        if isinstance(other, Airplane):
            if self.max_passenger < other.max_passenger:
                return True
            else:
                return False
        else:
            return 'Неверный выбор операндов.'

    # "<="
    def __le__(self, other):
        if isinstance(other, Airplane):
            if self.max_passenger <= other.max_passenger:
                return True
            else:
                return False
        else:
            return 'Неверный выбор операндов.'

    # ">"
    def __gt__(self, other):
        if isinstance(other, Airplane):
            if self.max_passenger > other.max_passenger:
                return True
            else:
                return False
        else:
            return 'Неверный выбор операндов.'

    # ">="
    def __ge__(self, other):
        if isinstance(other, Airplane):
            if self.max_passenger >= other.max_passenger:
                return True
            else:
                return False
        else:
            return 'Неверный выбор операндов.'

    def __str__(self):
        return f'{self.name} (маскимальное кол-во: {self.max_passenger})'

    def __int__(self):
        return self.current_passenger


airplane1 = Airplane('Boeing 777', 340, 310)
airplane2 = Airplane('Ту-154', 180, 180)
airplane3 = Airplane('Boeing 777', 340, 324)
print('Объекты: ', str(airplane1), ', ', str(airplane2), ', ', str(airplane3))
print('Число пасажиров на борту', airplane1.name, '= ', int(airplane1))
print(f'Сравнение типов {airplane1.name} и {airplane2.name}: ', airplane1.name == airplane2.name)
print(f'Сравнение типов {airplane1.name} и {airplane3.name}: ', airplane1.name == airplane3.name)
print('Текущее кол-во пассажиров = ', airplane1.current_passenger)
count1 = airplane1.current_passenger + 1
print('Значение сложения кол-ва пассажиров и 1 = ', count1)
count1 = 1 + airplane1.current_passenger
print('Значение сложения 1 и кол-ва пассажиров = ', count1)
count1 = airplane1.current_passenger - 1
print('Значение вычитания кол-ва пассажиров и 1 = ', count1)
count1 = 1 - airplane1.current_passenger
print('Значение вычитания 1 и кол-ва пассажиров = ', count1)
airplane1.current_passenger += 10
print('Значение текущего кол-ва пассажиров после сложения = ', airplane1.current_passenger)
airplane1.current_passenger -= 10
print('Значение текущего кол-ва пассажиров после вычитания = ', airplane1.current_passenger)
print('Сравнение максимального кол-ва самолетов (340 > 340):', airplane1 > airplane3)
print('Сравнение максимального кол-ва самолетов (340 < 340):', airplane1 < airplane3)
print('Сравнение максимального кол-ва самолетов (340 >= 340):', airplane1 >= airplane3)
print('Сравнение максимального кол-ва самолетов (340 <= 340):', airplane1 <= airplane3)
print(3 < airplane1)
