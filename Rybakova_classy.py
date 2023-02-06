list_auto = []


class Auto:
    objCount = 0

    def __init__(self, model, year, maker, power, color, price):
        self.model = model
        self.year = year
        self.maker = maker
        self.power = power
        self.color = color
        self.price = price

# УДАЛЕНО
    # def add_auto(auto_user):
    #     u_model = input('Введите модель: ')
    #     u_year = input('Введите год выпуска: ')
    #     u_maker = input('Введите производителя: ')
    #     u_power = input('Введите мощность двигателя: ')
    #     u_color = input('Введите цвет: ')
    #     u_price = input('Введите цену: ')
    #     auto_user = Auto(u_model, u_year, u_maker, u_power, u_color, u_price)
    #     list_auto.append(auto_user)
# вывод информации по объекту
    def output_ob(self):
        for i in self.__dict__:
            print(i, self.__dict__[i])

    def re_mod(self, new_model):
        self.model = new_model

    def re_year(self, new_year):
        self.year = new_year

    def re_maker(self, new_maker):
        self.maker = new_maker

    def re_power(self, new_power):
        self.model = new_power

    def re_color(self, new_color):
        self.color = new_color

    def re_price(self, new_price):
        self.price = new_price


auto1 = Auto('Lada', '2020', 'Russia', '123', 'White', '1231231')
auto2 = Auto('Toyota', '2015', 'Japan', '234', 'Black', '210567')
auto3 = Auto('Aidi', '2019', 'Germany', '765', 'black', '232563')
list_auto.extend([auto1, auto2, auto3])

while True:
    print('Выберите действие:')
    print('1 - Отобразить перечень объектов.')
    print('2 - Добавить объект.')
    print('3 - Изменить информацию по объекту.')
    print('4 - Отобразить инфрмацию по объекту.')
    print('5 - Добавить атрибут.')
    key = input('>>>> ')
    if key == '1':
        for i in list_auto:
            print('Номер по списку: ', list_auto.index(i) + 1)
            print(i.output_ob())
    elif key == '2':
        print('Метод удален.')
    elif key == '3':
        obj = input('Введите порядковый номер объекта: ')
        k = int(obj) - 1
        form = input('Введите характеристку для ввода нового значения (модель - 1, год выпуска - 2, производитель - 3,'
                     'мощность двигателя - 4, цвет - 5, цена - 6): ')
        if form == '1':
            list_auto[k].re_mod(input('Новое значение - '))
        elif form == '2':
            list_auto[k].re_year(input('Новое значение - '))
        elif form == '3':
            list_auto[k].re_maker(input('Новое значение - '))
        elif form == '4':
            list_auto[k].re_power(input('Новое значение - '))
        elif form == '5':
            list_auto[k].re_color(input('Новое значение - '))
        elif form == '6':
            list_auto[k].re_price(input('Новое значение - '))

    elif key == '4':
        obj = input('Введите порядковый номер объекта: ')
        k = int(obj) - 1
        list_auto[k].output_ob()
    elif key == '5':
        obj = input('Введите порядковый номер объекта: ')
        k = int(obj) - 1
        new_atr = input('Введите название нового атрибута: ')
        new_val = input('Введите его значение: ')
        setattr(list_auto[k], new_atr, new_val)
    else:
        print('Выход.')
        break
