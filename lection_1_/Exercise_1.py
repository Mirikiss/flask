from flask import Flask, render_template

app = Flask(__name__)

@app.get('/Hi')
def hi():
    return f'Hello world'


@app.get('/about/')
def about():
    return f'Добавили  функцию about'

@app.get('/contact/')
def contact():
    return f'Добавили  функцию contact'

@app.get('/summa/<int:a>/<int:b>')
def summa(a, b):
    return f'сумма двух числе {a+b}'

@app.get('/len/<string:a>')
def long_str(a):
    return f'Длина строки {len(a)}'

html = '''  <h1> Моя первая HTML страница</h1>
            <p>Знакомство с Flask </p> '''

@app.get('/str')
def show_string():
    return html

# Задание №6
# Написать функцию, которая будет выводить на экран HTML
# страницу с таблицей, содержащей информацию о студентах.
# Таблица должна содержать следующие поля: "Имя",
# "Фамилия", "Возраст", "Средний балл".
# Данные о студентах должны быть переданы в шаблон через
# контекст.

students = [
    {"name": "Макс", "surname": "Лепс", "age": 24, "reting": 3},
    {"name": "Макс", "surname": "Лепс", "age": 22, "reting": 3},
    {"name": "Макс", "surname": "Лепс", "age": 21, "reting": 3}
    ]
@app.route('/students/')
def get_udents():
    return render_template('students.html', students=students)

# Задание №7
# Написать функцию, которая будет выводить на экран HTML
# страницу с блоками новостей.
# Каждый блок должен содержать заголовок новости,
# краткое описание и дату публикации.
# Данные о новостях должны быть переданы в шаблон через
# контекст.


news = [
    {'name': 'Питомцы', 'data': '19.44.22', 'info': 'Пшитики'},
    {'name': 'Кот', 'data': '19.44.22', 'info': 'Пшитики'},
    {'name': 'Птица', 'data': '19.44.22', 'info': 'Пшитики'},
]

@app.route('/news/')
def news_paper():
    return render_template('news.html', news=news)

# Задание №8
# Создать базовый шаблон для всего сайта, содержащий
# общие элементы дизайна (шапка, меню, подвал), и
# дочерние шаблоны для каждой отдельной страницы.
# Например, создать страницу "О нас" и "Контакты",
# используя базовый шаблон.




if __name__ == '__main__':
    app.run(debug=True)