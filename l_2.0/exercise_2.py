# Задание №1
# Создать страницу, на которой будет кнопка "Нажми меня", при
# нажатии на которую будет переход на другую страницу с
# приветствием пользователя по имени.


from flask import Flask, render_template, request, redirect, url_for
from pathlib import PurePath, Path
from werkzeug.utils import secure_filename


app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/hello')
def hello():
    return f'Hello!!!'

# Задание №2
# Создать страницу, на которой будет изображение и ссылка
# на другую страницу, на которой будет отображаться форма
# для загрузки изображений.

@app.route('/uploads', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files.get('file')
        file_name = secure_filename(file.filename)
        file.save(PurePath.joinpath(Path.cwd(), 'uploads', file_name))
        return f"Файл {file_name} загружен на сервер"
    return render_template('uploads.html')

# Задание №3
# Создать страницу, на которой будет форма для ввода логина
# и пароля
# При нажатии на кнопку "Отправить" будет произведена
# проверка соответствия логина и пароля и переход на
# страницу приветствия пользователя или страницу с
# ошибкой.

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        login = request.form.get('login')
        password = request.form.get('password')
        if login == 'Вася' and password == '123':
            return f'Добро пожаловать'
        return f'Ошибка'
    return render_template('login.html')

# Задание №4
# Создать страницу, на которой будет форма для ввода текста и
# кнопка "Отправить"
# При нажатии кнопки будет произведен подсчет количества слов
# в тексте и переход на страницу с результатом.

@app.route('/text', methods = ['GET', 'POST'])
def text():
    if request.method == 'POST':
        text = request.form.get('text')
        return f'Длина текста {len(text)}'
    return render_template('texts.html')


# Задание №5
# Создать страницу, на которой будет форма для ввода двух
# чисел и выбор операции (сложение, вычитание, умножение
# или деление) и кнопка "Вычислить"
# При нажатии на кнопку будет произведено вычисление
# результата выбранной операции и переход на страницу с
# результатом.

@app.route('/sum', methods = ['GET', 'POST'])
def sum1():
    if request.method == 'POST':
        num1 = request.form.get('num1')
        num2 = request.form.get('num2')
        operetion = request.form.get('Operation')
        if operetion == 'sum':
            return f'Сумма = {num1+num2}'
        elif operetion == 'sub':
            return f'Разность = {num1/num2}'
        elif operetion == 'mul':
            return f'Разность = {num1*num2}'
        elif operetion == 'sut':
            return f'Разность = {num1/num2}'
        elif operetion == 'div':
            return f'минус = {num1-num2}'
    return render_template('sum.html')

# Задание №7
# Создать страницу, на которой будет форма для ввода числа
# и кнопка "Отправить"
# При нажатии на кнопку будет произведено
# перенаправление на страницу с результатом, где будет
# выведено введенное число и его квадрат.

@app.route('/number', methods = ['GET', 'POST'])
def sum1():
    if request.method == 'POST':
        num1 = int(request.form.get('num1'))
        return redirect(url_for('qurter', number = num1**2))
    return render_template('number.html')


@app.route('/qurter/<int:number>')
def qurter(number):
    return f'{number}'

if __name__ == '__main__':
    app.run(debug=True)