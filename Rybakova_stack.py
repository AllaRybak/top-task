class StackStr:
    def __init__(self):
        self.stack = []
        self.max = 4
        self.len_st = 0

# помещение строки в стек
    def push(self, val: str):
        if self.len_st >= self.max:
            return f'Невозможно добавить, стек полон.'
        elif type(val) == str:
            self.stack.append(val)
            self.len_st += 1
            return f'Стек дополнен.'
        else:
            return f'Тип данных не строчный.'

# выталкивание строки из стека
    def get(self):
        if self.check_0():
            return None
        else:
            self.len_st -= 1
            return self.stack.pop()

# подсчет количества строк в стеке
    def count(self):
        return self.len_st

# проверка, пустой ли стек
    def check_0(self):
        if not self.len_st:
            return True
        else:
            return False

# проверка, полный ли стек
    def check_full(self):
        if self.len_st == self.max:
            return True
        else:
            return False

# очистка стека
    def clear(self):
        for i in range(self.len_st):
            self.stack.pop()
        self.len_st = 0

# получение значения без выталкивания верхней строки из стека
    def get_without_del(self):
        if self.check_0():
            return None
        else:
            return self.stack[-1]


stack1 = StackStr()
while True:
    print(f'В стеке {stack1.len_st} узла(ов) из {stack1.max} возможных. Выберите нужное действие: ')
    print('''
        1 - поместить строку в стек;
        2 - выталкнуть строку из стека;
        3 - подсчитать количество строк в стеке;)
        4 - проверить стек на пустоту;
        5 - проверить стек на полноту;
        6 - очистить стек;
        7 - получить значение без выталкивания верхней строки из стека.''')
    key = input('>>> ')
    if key == '1':
        val_user = input('Введите строку: ')
        print(stack1.push(val_user))
    elif key == '2':
        if not stack1.len_st:
            print('В стеке нет строк.')
        else:
            print(f'Строка {stack1.get()} из стека вытолкнута')
    elif key == '3':
        print('Текущая длина стека: ', stack1.len_st)
    elif key == '4':
        if stack1.check_0():
            print('Стек пуст.')
        else:
            print('Стек не пуст.')
    elif key == '5':
        if stack1.check_full():
            print('Стек полон.')
        else:
            print('Стек не полон.')
    elif key == '6':
        stack1.clear()
        print('Стек очищен.')
    elif key == '7':
        if not stack1.len_st:
            print('В стеке нет строк.')
        else:
            print('Последний узел стека: ', stack1.get_without_del())
    else:
        print('Вы вышли.')
        break

# print('Результат извелечения узла из пустого стека: ', stack1.get())
# print(f'Проверка на полноту стека: {stack1.check_full()}, проверка на его пустоту: {stack1.check_0()}.')
# print(stack1.push('1-я строка стэка.'))
# print(stack1.push('2-я строка стэка.'))
# print(stack1.push('3-я строка стэка.'))
# print(stack1.push('4-я строка стэка.'))
# print(stack1.push('5-я строка стэка.'))
# print(f'Проверка на полноту стека: {stack1.check_full()}, проверка на его пустоту: {stack1.check_0()}.')
# print('Текущая длина стека: ', stack1.len_st)
# print('Выталкивание узла из стэка: ', stack1.get())
# print('Текущая длина стека: ', stack1.len_st)
# print('Последний узел: ', stack1.get_without_del())
# print('Текущая длина стека: ', stack1.len_st)
# stack1.clear()
# print(f'Проверка на полноту стека: {stack1.check_full()}, проверка на его пустоту: {stack1.check_0()}.')
