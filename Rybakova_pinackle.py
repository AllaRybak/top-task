import pickle
import json

towns = ['Москва', 'Пекин', 'Петушки', 'Ростов-на-Дону', 'Волгоград', 'Санкт-Петербург', 'Дамаск', 'Челябинск',
         'Калининград', 'Минск', 'Анкара', 'Бразилиа']
class Airplane:
    def __init__(self, name: str, max_passenger: int, current_passenger: int, flight1: str, flight2: str):
        self.name = name
        self.max_passenger = max_passenger
        self.current_passenger = current_passenger
        self.flight1 = flight1
        self.flight2 = flight2

    @property
    def flight_start_end(self):
        return f'{self.flight1} - {self.flight2}'

    def __add__(self, other):
        return self.current_passenger + other

    def __sub__(self, other):
        return self.current_passenger - other

    def __iadd__(self, other):
        self.current_passenger += other
        return self

    def __isub__(self, other):
        self.current_passenger -= other
        return self

    def __radd__(self, other):
        return self.current_passenger + other

    def __eq__(self, other):
        if isinstance(other, Airplane):
            if self.name == other.name:
                return True
            else:
                return False
        else:
            return 'Неверный выбор операндов.'

    def __lt__(self, other):
        if isinstance(other, Airplane):
            if self.max_passenger < other.max_passenger:
                return True
            else:
                return False
        else:
            return 'Неверный выбор операндов.'

    def __le__(self, other):
        if isinstance(other, Airplane):
            if self.max_passenger <= other.max_passenger:
                return True
            else:
                return False
        else:
            return 'Неверный выбор операндов.'

    def __gt__(self, other):
        if isinstance(other, Airplane):
            if self.max_passenger > other.max_passenger:
                return True
            else:
                return False
        else:
            return 'Неверный выбор операндов.'

    def __ge__(self, other):
        if isinstance(other, Airplane):
            if self.max_passenger >= other.max_passenger:
                return True
            else:
                return False
        else:
            return 'Неверный выбор операндов.'

    def re_flight1(self, new_flight_start):
        if new_flight_start in towns:
            self.flight1 = new_flight_start
        else:
            print(new_flight_start, ' не входит в число допустимых городов перелёта.')

    def re_flight2(self, new_flight_end):
        if new_flight_end in towns:
            self.flight2 = new_flight_end
        else:
            print(new_flight_end, ' не входит в число допустимых городов перелёта.')

    def __str__(self):
        return f'{self.name}, {self.flight_start_end} (маскимальное кол-во: {self.max_passenger})'

    def __int__(self):
        return self.current_passenger

# запись в picle
    def to_pickle(self):
        return pickle.dumps(self.__dict__)

# запись в json
    def to_json(self):
        return json.dumps(self.__dict__, ensure_ascii=False)


airplane1 = Airplane('Boeing 777', 340, 310, 'Москва', 'Пекин')
airplane2 = Airplane('Ту-154', 180, 180, 'Москва', 'Петушки')
print(airplane2)
airplane2.re_flight2('London')
airplane1.re_flight1('Ростов-на-Дону')
# упаковка/распаковка pickle
buf_p = airplane1.to_pickle()
with open('Text_files/testAir.pkl', 'wb') as file:
    pickle.dump(buf_p, file)
with open('Text_files/testAir.pkl', 'rb') as file:
    new_test_dict = pickle.load(file)
    text_pkl = pickle.loads(new_test_dict)
print('Pickle: ', text_pkl)
# упаковка/распаковка json
buf_j = airplane2.to_json()
with open('Text_files/testAir.json', 'w', encoding='cp1251') as file:
    file.write(buf_j)
with open('Text_files/testAir.json', 'r') as file:
    new_test_dict1 = json.load(file)
print('Jason:', new_test_dict1)
