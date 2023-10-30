from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request, render_template
from model import Student, db, Faculty

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db.init_app(app)


@app.cli.command("init-db")
def init_db():
    db.create_all()
    print('OK')

@app.route('/')
def hi():
    students = Student.query.all()
    return render_template('index.html', students=students)


def add_test_data():
    for i in range(5):
        faculty = Faculty(name = f'faculty{i}')
        db.session.add(faculty)
        for j in range(5):
            studen = Student(
                name = 'db',
                firstname = 'lo',
                age = 31,
                sex = 'vi',
                group = 5,
                faculty_id = i
            )
            db.session.add(studen)
    db.session.commit()
    print(f'данные добавлены')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        add_test_data()
    app.run(debug=True)






# Задание №1
# Создать базу данных для хранения информации о студентах университета.
# База данных должна содержать две таблицы: "Студенты" и "Факультеты".
# В таблице "Студенты" должны быть следующие поля: id, имя, фамилия,
# возраст, пол, группа и id факультета.
# В таблице "Факультеты" должны быть следующие поля: id и название
# факультета.
# Необходимо создать связь между таблицами "Студенты" и "Факультеты".
# Написать функцию-обработчик, которая будет выводить список всех
# студентов с указанием их факультета.