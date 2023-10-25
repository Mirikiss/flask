# Задание №9
# Создать базовый шаблон для интернет-магазина,
# содержащий общие элементы дизайна (шапка, меню,
# подвал), и дочерние шаблоны для страниц категорий
# товаров и отдельных товаров.
# Например, создать страницы "Одежда", "Обувь" и "Куртка",
# используя базовый шаблон.


from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/main')
def title():
    text = {'title': 'Главная'}
    return render_template('main.html', **text)

clothes = [
    {'name': 'Брюки', 'size': '42', 'color': 'Синий', 'count': '5'},
    {'name': 'Шорты', 'size': '45', 'color': 'Черный', 'count': '12'},
    {'name': 'Майка', 'size': '38', 'color': 'белая', 'count': '8'},
    {'name': 'Рубашка', 'size': '48', 'color': 'Голубой', 'count': '3'},
]

@app.route("/clothes")
def list_clothes():
    return render_template('clothes.html', clothes=clothes)

footwear = [
    {'name': 'Туфли', 'size': '41-45', 'color': 'черные', 'count': '15'},
    {'name': 'Кроссовки', 'size': '36-42', 'color': 'белый', 'count': '20'},
    {'name': 'Мокасины', 'size': '40-43', 'color': 'синий', 'count': '8'},
    {'name': 'Лоферы', 'size': '42-43', 'color': 'коричневые', 'count': '3'}
]

@app.route("/footwear")
def list_footwear():
    return render_template('footwear.html', footwear=footwear)

jacket = [
    {'name': 'Пуховик', 'size': '41-45', 'color': 'черные', 'count': '15'},
    {'name': 'Пальто', 'size': '36-42', 'color': 'белый', 'count': '20'},
    {'name': 'Ветровка', 'size': '40-43', 'color': 'синий', 'count': '8'}
]

@app.route("/jacket")
def list_jacket():
    return render_template('jacket.html', jacket=jacket)


if __name__=='__main__':
    app.run(debug=True)