from flask import Flask, render_template, request
from markupsafe import escape
from werkzeug.utils import secure_filename
from pathlib import PurePath, Path


app = Flask(__name__)

# Задание №1
# Создать страницу, на которой будет кнопка "Нажми меня", при
# нажатии на которую будет переход на другую страницу с
# приветствием пользователя по имени.

@app.route('/')
def push():
    return render_template('form.html')

@app.route('/hello')
def hello():
    return f'Hello!!!'

# Задание №2
# Создать страницу, на которой будет изображение и ссылка
# на другую страницу, на которой будет отображаться форма
# для загрузки изображений.

@app.route('/load', methods = ["GET", "POST"])
def load():
    if request.method == 'POST':
        file = request.files.get('file')
        file_name = secure_filename(file.filename)
        file.save(PurePath.joinpath(Path.cwd(), 'uploads', file_name))
        return f'Загрузка на сервер {file_name}'
    return render_template('uploads.html')

# Задание №3
# Создать страницу, на которой будет форма для ввода логина
# и пароля
# При нажатии на кнопку "Отправить" будет произведена
# проверка соответствия логина и пароля и переход на
# страницу приветствия пользователя или страницу с
# ошибкой.

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        login = request.form.get('login')
        password = request.form.get('password')
        if login == 'q' and password == '123':
            return f'Good morning'
        return 'Error'
    return render_template('login.html')


# Задание №4
# Создать страницу, на которой будет форма для ввода текста и
# кнопка "Отправить"
# При нажатии кнопки будет произведен подсчет количества слов
# в тексте и переход на страницу с результатом.

@app.route('/long', methods = ['GET', 'POST'])
def long():
    if request.method == 'POST':
        text = request.form.get('text')
        return f'count {len(text)}'    
    return render_template('long.html')


# @app.route('/<path:file>/')
# def get(file):
#     return f'Ваш фаил {escape(file)}'

# @app.route('/sobmit', methods = ['GET, POST'])
# def submit():
#     if request.method == 'POST':
#         name = request.form.get('name')
#         return f'Hello {name}'
#     return render_template('get.html')

# @app.route('/submit', methods=['GET', 'POST'])
# def submit():
#     if request.method == 'POST':
#         name = request.form.get('name')
#         return f'Hello {name}!'
#     return render_template('form.html')





if __name__ == '__main__':
    app.run(debug=True)