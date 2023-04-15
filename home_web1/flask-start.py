from flask import Flask, render_template, request, flash, session, redirect, url_for, abort
# import templates

app = Flask(__name__)
app.config['SECRET_KEY'] = 'fdgdfgdfggf786hfg6hfg6h7f'

menu = [{'name': 'Нечетные числа', 'url': 'nechet'},
        {'name': 'Четные числа', 'url': 'chet'},
        {'name': 'Обратная связь', 'url': 'contact'},
        {'name': 'Регистрация', 'url': 'login'}
        ]


@app.route('/')
@app.route('/start')
def index():
    return render_template('index.html', the_title='Домашнее задание от 06.04.2023', menu=menu)

# ввод данных для подсчета нечетных


@app.route('/nechet')
def nechet():
    return render_template('nechet.html', title='Диапазон для вывода нечетных значений.')

# ввод данных для подсчета нечетных


@app.route('/chet')
def chet():
    return render_template('chet.html', title='Диапазон для вывода четных значений.')

# вывод нечетных


@app.route('/resaults', methods=['POST'])
def resaults():
    start = int(request.form['number_1_n'])
    finish = int(request.form['number_2_n'])
    if start <= finish:
        res = [i for i in range(start, finish + 1) if i % 2]
        return render_template('resaults.html', res=f'Нечетные числа в диапазоне [{start}, {finish}]: {str(res)}')
    else:
        return render_template('resaults.html', res='Ошибка ввода данных.')


# вывод нечетных


@app.route('/resaults_chet', methods=['POST'])
def results_chet():
    start = int(request.form['number_1_c'])
    finish = int(request.form['number_2_c'])
    if start <= finish:
        res = [i for i in range(start, finish + 1) if not i % 2]
        return render_template('resaults_chet.html', res=f'Четные числа в диапазоне [{start}, {finish}]: {str(res)}')
    else:
        return render_template('resaults_chet.html', res='Ошибка ввода данных.')


@app.route('/contact', methods=['POST', 'GET'])
def contact():
    if request.method == 'POST':
        if len(request.form['username']) > 2:
            flash('Сообщение отправлено', category='success')
            user_text = request.form['message']
            with open('./text.txt', 'a') as file:
                file.write(user_text + '\n')
        else:
            flash('Ошибка отправки', category='error')
    return render_template('contact.html')


# авторизация

@app.route("/login", methods=['POST', 'GET'])
def login():
    if 'userLogged' in session:
        return redirect(url_for('profile', username=session['userLogged']))
    elif request.method == 'POST' and request.form['username'] == "top" and request.form['psw'] == "2023":
        session['userLogged'] = request.form['username']
        return redirect(url_for('profile', username=session['userLogged']))

    return render_template('login.html', title="Авторизация", menu=menu)

# авторизованная страница


@app.route("/profile/<username>")
def profile(username):
    if 'userLogged' not in session or session['userLogged'] != username:
        abort(401)
    return f"Страница с авторизованным пользователем: {username}"


@app.errorhandler(404)
def page_not_found():
    return render_template('page404.html', title="Страница не найдена", menu=menu), 404


app.run(debug=True)
