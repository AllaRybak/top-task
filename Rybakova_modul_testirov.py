class IntElements:
    def __init__(self):
        pass

    @staticmethod
    def type_of(funk):
        def wrapper(self, *args):
            for i in args:
                if type(i) != int:
                    return 'Error'
            return funk(self, *args)
        return wrapper

    @type_of
    def sum_int(self, *args):
        return sum(args)

    @type_of
    def arifm_middle(self, *args):
        return sum(args)/len(args)

    @type_of
    def maxim(self, *args):
        return max(args)

    @type_of
    def mini(self, *args):
        return min(args)


int_user = IntElements()
print(f'Сумма: ', int_user.sum_int(1, 0, 100, 45, 34))
print(f'Среднее арифметическое: ', int_user.arifm_middle(5, 2, 4))
print(f'Минимальное: ', int_user.mini(1, 0, -10))
