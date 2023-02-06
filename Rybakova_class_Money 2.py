class Money:
    def __init__(self, currency: str, int_part: int, float_part: int, symbol_currency: str):
        self.currency = currency
        self.int_part = int_part
        self.float_part = float_part
        self.symbol_currency = symbol_currency

    @property
    def unite_currency(self):

        return self.int_part + self.float_part // 100 + (self.float_part % 100) / 100

    def output_currency(self):
        print('Результат декоратора: ', self.unite_currency, self.symbol_currency, end='')
        print()


money1 = Money('Рубль', 12, 135, '₽')
money2 = Money('Юань', 10056, 3, ' ¥')
money3 = Money('Фунт', 0, 234, '£')
for i in money1.__dict__:
    print(i, ':', money1.__dict__[i])
money1.output_currency()
for i in money2.__dict__:
    print(i, ':', money2.__dict__[i])
money2.output_currency()
for i in money3.__dict__:
    print(i, ':', money3.__dict__[i])
money3.output_currency()
