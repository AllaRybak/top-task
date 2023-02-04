import csv
fild_nam = ['Фамилия', 'Имя', 'Отчество', 'Возраст', 'Телефон']
while True:
    print('''Выберите нужный пункт:'
          '0 - Читать файл;'
          '1 - Добавить сотрудника;'
          '2 - Удалить сотрудника;'
          '3 - Править данные сотрудника;'
          '4 - Поиск сотрудников по первой букве фамилии;'
          '5 - Поиск сотрудников по возрасту;'
          'Q - Выход''')
    key = input('--> ')
    # ____READ
    # user_file = input('Введите имя файла сотрудников: ') # '22dec-workers.csv'
    # with open(user_file, encoding='windows-1251') as file_main:
    if key == '0':
        with open('Text_files/22dec-workers.csv', encoding='windows-1251') as file_main:
            reader = csv.reader(file_main, delimiter=',')
            count = 0
            for row in reader:
                if not count:
                    header = '\t'.join(row)
                    # header_list = ' '.join(row).split()
                    print(header)
                else:
                    print('\t'.join(row))
                count += 1
    # ____ADD
    if key == '1':
        new_worker = [input('Фамилия: '), input('Имя: '), input('Отчество: '),
                      input('Возраст: '), input('Телефон: ')]
        # with open(user_file, 'a', encoding='windows-1251') as file_main:
        with open('Text_files/22dec-workers.csv', 'a', encoding='windows-1251') as file_main:
            writer = csv.writer(file_main, delimiter=',', lineterminator='\r')
            writer.writerow(new_worker)
        print(f'Сотрудник добавлен в файл.')
    # ____DELETE
    elif key == '2':
        del_worker_sname = input('Введите фамилию удаляемого сотрудника: ')
        # with open(user_file, encoding='windows-1251') as file_main:
        with open('Text_files/22dec-workers.csv', encoding='windows-1251') as file_main:
            actual_worker = []
            reader = csv.DictReader(file_main, delimiter=',')
            for row in reader:
                s = 0
                if row['Фамилия'] != del_worker_sname:
                    actual_worker.append(row)
                    s += 1
        if s:
            print('В файле нет сотрудника с такой фамилией.')
        else:
            # with open(user_file, 'w', encoding='windows-1251') as file_main:
            with open('Text_files/22dec-workers.csv', 'w', encoding='windows-1251') as file_main:
                writer = csv.DictWriter(file_main, fieldnames=fild_nam)
                writer.writeheader()
                writer.writerows(actual_worker)
            print(f'Сотрудник {del_worker_sname} из файла удален.')
    # ____EDIT
    elif key == '3':
        try:
            edit_worker = input('Введите фамилию сотрудника, чьи данные необходимо исправить: ')
            # with open(user_file, encoding='windows-1251') as file_main:
            with open('Text_files/22dec-workers.csv', encoding='windows-1251') as file_main:
                actual_data = []
                reader = csv.DictReader(file_main, delimiter=',')
                edit_column = input('Введите название позиции (Фамилия, Имя, Отчество, Возраст, Телефон): ')
                if edit_column not in fild_nam:
                    raise ValueError
                else:
                    new_data = input(f'Введите новые данные для "{edit_column}": ')
                    s = 0
                    for row in reader:
                        if row['Фамилия'] == edit_worker:
                            row[f'{edit_column}'] = new_data
                            s += 1
                        actual_data.append(row)
            if not s:
                print('Сотрудника с такой фамилией нет в списке.')
            else:
                # with open(user_file, 'w', encoding='windows-1251') as file_main:
                with open('Text_files/22dec-workers.csv', 'w', encoding='windows-1251') as file_main:
                    writer = csv.DictWriter(file_main, fieldnames=fild_nam)
                    writer.writeheader()
                    writer.writerows(actual_data)
                print(f'Изменения внесены.')
        except ValueError:
            print('Ошибка ввода.')

    # ____search
    elif key == '4':
        first_s = input('Введите первую букву фамилии для поиска сотрудников: ')
        # with open(user_file, encoding='windows-1251') as file_main:
        with open('Text_files/22dec-workers.csv', encoding='windows-1251') as file_main:
            out_data = []
            reader = csv.DictReader(file_main, delimiter=',')
            for row in reader:
                if row['Фамилия'][0] == first_s:
                    out_data.append(row)
        if not len(out_data):
            print(f'Сотрудников с фамилией на букву "{first_s}" нет в файле.')
        else:
            # with open(user_file, 'w', encoding='windows-1251') as file_main:
            with open('Text_files/22dec-workers_search_f.csv', 'w', encoding='windows-1251') as file_main:
                writer = csv.DictWriter(file_main, fieldnames=fild_nam)
                writer.writeheader()
                writer.writerows(out_data)
            print(f'Создан файл с сотрудниками с фамилией на букву {first_s}.')
    # ____SEARCH_AGE
    elif key == '5':
        search_age = input('Введите возраст для поиска сотрудников: ')
        # with open(user_file, encoding='windows-1251') as file_main:
        with open('Text_files/22dec-workers.csv', encoding='windows-1251') as file_main:
            out_data = []
            reader = csv.DictReader(file_main, delimiter=',')
            for row in reader:
                if row['Возраст'] == search_age:
                    out_data.append(row)
        if not len(out_data):
            print(f'Сотрудников с таким возрастом нет в файле.')
        else:
            # with open(user_file, 'w', encoding='windows-1251') as file_main:
            with open('Text_files/22dec-workers_age.csv', 'w', encoding='utf-8') as file_main:
                writer = csv.DictWriter(file_main, fieldnames=fild_nam)
                writer.writeheader()
                writer.writerows(out_data)
            print(f'Создан файл с сотрудниками возраста - {search_age}.')
    elif key == 'Q':
        break
