import string


class Number:
    def __init__(self, value=None):
        self.value = value

    @staticmethod
    def type_of(funk):
        def wrapper(self, a):
            if type(a) != int:
                return 'Error'
            return funk(self, a)
        return wrapper

    def read_write(self):
        numb = input('Запись числа >>>')
        if numb:
            for i in numb:
                if i not in string.digits:
                    return 'Error'
            self.value = int(numb)
            return int(numb)
        else:
            return 'Error'

    @type_of
    def num22(self, num):
        if num >= 0:
            return bin(num)[2:]
        else:
            return '-' + bin(num)[3:]

    @type_of
    def num28(self, num):
        if num >= 0:
            return oct(num)[2:]
        else:
            return '-' + oct(num)[3:]

    @type_of
    def num216(self, num):
        if num >= 0:
            return hex(num)[2:]
        else:
            return '-' + hex(num)[3:]


num_user = Number()
print('Перевод в двоичную систему: ', num_user.num22(-90))
print('Перевод в восьмеричную: ', num_user.num28(-90))
print('Перевод в шестнадцатеричную: ', num_user.num216(-90))
print('Чтение числа: ', num_user.read_write())
print(f'Перевод {num_user.value} в двоичную систему: ', num_user.num22(num_user.value))
print(f'Перевод {num_user.value} в восьмеричную: ', num_user.num28(num_user.value))
print(f'Перевод {num_user.value} в шестнадцатеричную: ', num_user.num216(num_user.value))
