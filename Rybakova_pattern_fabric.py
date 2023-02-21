from abc import ABC, abstractmethod


class Product(ABC):
    @abstractmethod
    def type_paste(self):
        pass

    @abstractmethod
    def sauce(self):
        pass

    @abstractmethod
    def filling(self):
        pass

    @abstractmethod
    def supplement(self):
        pass


class PasteBukatini(Product):
    def __init__(self, sauce_u: str, suppl: str):
        self.sauce_u = sauce_u
        self.suppl = suppl

    def type_paste(self):
        return f'Паста типа Букатини.'

    def sauce(self):
        return f'Добавлен соус - {self.sauce_u}.'

    def filling(self):
        return f'Без начинки.'

    def supplement(self):
        return f'С добавкой - {self.suppl}.'

    def __str__(self):
        return f'{self.type_paste()} {self.sauce()} {self.filling()} {self.supplement()}'


class PasteLazagna(Product):
    def __init__(self, fill: str, suppl: str):
        self.fill = fill
        self.suppl = suppl

    def type_paste(self):
        return f'Паста типа Лазанья.'

    def sauce(self):
        return f'Без соуса.'

    def filling(self):
        return f'Начинка - {self.fill}.'

    def supplement(self):
        return f'С добавкой - {self.suppl}.'

    def __str__(self):
        return f'{self.type_paste()} {self.sauce()} {self.filling()} {self.supplement()}'


class PasteSpaghetti(Product):
    def __init__(self, sauce_u: str, suppl: str):
        self.sauce_u = sauce_u
        self.suppl = suppl

    def type_paste(self):
        return f'Паста типа Спагетти.'

    def sauce(self):
        return f'Добавлен соус - {self.sauce_u}.'

    def filling(self):
        return f'Без начинки.'

    def supplement(self):
        return f'С добавкой - {self.suppl}.'

    def __str__(self):
        return f'{self.type_paste()} {self.sauce()} {self.filling()} {self.supplement()}'


class PasteFactory:
    def get_paste(self, type_paste, *args):
        if type_paste == 'PasteBukatini':
            return PasteBukatini(args[0], args[1])
        elif type_paste == 'PasteLazagna':
            return PasteLazagna(args[0], args[1])
        elif type_paste == 'PasteSpaghetti':
            return PasteSpaghetti(args[0], args[1])


factory = PasteFactory()
paste1 = factory.get_paste('PasteLazagna', 'Фарш', 'Перец')
paste2 = factory.get_paste('PasteSpaghetti', 'Песто', 'Паприка')
print(paste1)
print(paste2)
