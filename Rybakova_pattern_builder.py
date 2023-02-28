from abc import ABC, abstractmethod


class Paste:
    def __init__(self):
        self.sauce = None  # соус
        self.filling = None  # начинка
        self.supplement = None  # добавки
        self.detect_fish = []

    def __str__(self):
        string = 'Состав нашей пасты: \n'
        # if self.sauce:
        #     string += '- соус.\n'
        # if self.filling:
        #     string += '- с начинкой.\n'
        # if self.supplement:
        #     string += '- с добавками.\n'
        # self.detect_fish
        # string += 'В пасте: \n'
        for i in self.detect_fish:
            string += '   ' + str(i) + '\n'
        return string


class Sauce:
    def __str__(self):
        return f'Соус'


class Filling:
    def __str__(self):
        return f'Начинка'


class Supplement:
    def __str__(self):
        return f'Добавка'


class PasteBuilder(ABC):
    @abstractmethod
    def __init__(self):
        self.product = Paste()

    @abstractmethod
    def reset(self):
        self.product = Paste()

    @abstractmethod
    def build_dish(self):
        pass


class PasteLasagna(PasteBuilder):
    def __init__(self):
        super(PasteLasagna, self).__init__()

    def reset(self):
        super(PasteLasagna, self).reset()

    def build_dish(self, *args):
        self.product.detect_fish.append(f'- {Sauce()}: {args[0]}')
        self.product.detect_fish.append(f'- {Filling()}: {args[1]}')
        self.product.sauce = True
        self.product.filling = True

    def __str__(self):
        str_spag = 'Тип пасты - лазанья. \n' + self.product.__str__()
        return str_spag


lasagna_standart = PasteLasagna()
lasagna_standart.build_dish('Соевый', 'Фарш')
print(lasagna_standart)


class PasteSpaghetti(PasteBuilder):
    def __init__(self):
        super(PasteSpaghetti, self).__init__()

    def reset(self):
        super(PasteSpaghetti, self).reset()

    def build_dish(self, *args):
        self.product.detect_fish.append(f'- {Sauce()}: {args[0]}')
        self.product.detect_fish.append(f'- {Supplement()}: {args[1]}')
        self.product.sauce = True
        self.product.supplement = True

    def __str__(self):
        str_spag = 'Тип пасты - спагетти. \n' + self.product.__str__()
        return str_spag


spaghetti_standart = PasteSpaghetti()
spaghetti_standart.build_dish('Томатный', 'Паприка')
print(spaghetti_standart)
spaghetti_standart.build_dish('Гранатовый', 'Зелень')
print(spaghetti_standart)
