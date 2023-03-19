import threading
from datetime import datetime
import random

# начальный список, путь к файлу, список простых
list_num = []
treck = ''
list_num_simple = []

# _____ вспомогательные ф-ции (простое число и факториал)


def simple(n: int) -> bool:
    for i in range(2, n):
        if not n % i:
            return False
    return True


def factorial(n: int) -> int:
    if n == 1:
        return n
    else:
        return n * factorial(n-1)

# ____________________


def input_file(event):
    global treck
    treck = input('Введите путь к файлу: ')
    event.set()
    time0 = datetime.now()
    print('Создание файла: ', time0)


def potok1_random(event, event2):
    event.wait()
    global list_num
    global treck
    list_num = [random.randint(1, 100) for _ in range(20)]
    with open(treck, 'w') as file:
        for i in list_num:
            file.write(str(i) + ' ')
    event2.set()
    time0 = datetime.now()
    print('Старт потока 1: ', time0)


def potok2_simple(event2):
    event2.wait()
    global list_num
    global treck
    global list_num_simple
    if treck:
        with open(treck) as file:
            list_num = list(file.read().split())
    for i in list_num:
        if simple(int(i)):
            list_num_simple.append(int(i))
    with open('Text_files/potok_simple.txt', 'w') as f:
        f.write(str(list_num_simple))
    time0 = datetime.now()
    print('Старт потока 2: ', time0)


def potok3_factorial(event2):
    event2.wait()
    global list_num
    global treck
    if treck:
        with open(treck) as file:
            list_num = list(file.read().split())
    buf = []
    for i in list_num:
        buf.append(factorial(int(i)))
    with open('Text_files/potok_factorial.txt', 'w') as f:
        for num in buf:
            f.write(str(num) + '\n')
    time0 = datetime.now()
    print('Старт потока 3: ', time0)


e1 = threading.Event()
e2 = threading.Event()
p0 = threading.Thread(target=input_file, args=[e1])
p1 = threading.Thread(target=potok1_random, args=[e1, e2])
p2 = threading.Thread(target=potok2_simple, args=[e2])
p3 = threading.Thread(target=potok3_factorial, args=[e2])
p0.start()
p1.start()
p2.start()
p3.start()
