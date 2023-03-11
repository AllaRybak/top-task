import sys


class Article:
    def __init__(self, name, author, count_symbol, first_name_edition='', description=''):
        self.name = name
        self.author = author
        self.count_symbol = count_symbol
        self.first_name_edition = first_name_edition
        self.description = description

    def __str__(self):
        return f'Статья "{self.name}" от автора {self.author}'


class Model:
    @staticmethod
    def _read_txt(path):
        data = []
        with open(path, encoding='windows-1251') as f:
            for line in f:
                data.append(line.replace('\n', ''))
        return data

    @staticmethod
    def _str_to_article(list_text):
        data = []
        for line in list_text:
            buf = Article(*line.split(';'))
            data.append(buf)
        return data

    @staticmethod
    def new_article(path):
        data = Model._read_txt(path)
        return Model._str_to_article(data)

    @staticmethod
    def add_new_article(path, text_user):
        with open(path, 'a', encoding='windows-1251') as f:
            f.writelines('\n' + text_user)

    @staticmethod
    def count_article_1_author(path, text_user):
        res = 0
        with open(path, encoding='windows-1251') as f:
            for line in f:
                plist = line.split(';')
                if plist[1] == text_user:
                    res += 1
        return res


class View:
    @staticmethod
    def print_list(plist):
        for i in plist:
            print(i)

    @staticmethod
    def print_select_menu():
        print('Выбор действия:')
        print('1 - вывести список статей;')
        print('2 - добавить статью;')
        print('3 - посчитать количество статей одного автора;')
        print('0 - выход.')

    @staticmethod
    def print_add_user_article():
        print('Введите данные в формате: Название статьи;Автор;Количество символов в статье;'
              'Издательство;Краткое описание')

    @staticmethod
    def print_author():
        print('Введите автора (как в перечне):')

    @staticmethod
    def print_count_article(count, author):
        print(f'Имеется {count} статей от автора {author}.')

    @staticmethod
    def print_error():
        print('Ошибка ввода данных либо значений не найдено.')


class Controller:
    @staticmethod
    def menu():
        View.print_select_menu()
        buf = input('>>> ')
        if buf == '1':
            res = Model.new_article('Text_files/1mvc.txt')
            View.print_list(res)
        elif buf == '2':
            View.print_add_user_article()
            user_article = input()
            if user_article.count(';') < 2 or user_article.count(';') > 4:
                View.print_error()
            else:
                Model.add_new_article('Text_files/1mvc.txt', user_article)
        elif buf == '3':
            View.print_author()
            user_author = input()
            buf = Model.count_article_1_author('Text_files/1mvc.txt', user_author)
            if buf:
                View.print_count_article(buf, user_author)
            else:
                View.print_error()
        elif buf == '0':
            sys.exit()


while True:
    Controller.menu()
