from flask import Flask, render_template
from models import Student, Faculty, db, datetime, SQLAlchemy
from random import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db.init_app(app)

@app.route('/')
def main():
    students = Student.query.all()
    return render_template('inex.html', students=students)

@app.cli.command("init-db")
def init_db():
    db.create_all()
    print('OK')


def add_user():
    for i in range(5):
        faculty = Faculty(name = f'faculty{i}')
        db.session.add(faculty)
        for j in range(5):
            studen = Student(
                name = 'Пвел' + ' ' + str(i),
                firstname = 'Заяц' + ' ' + str(j),
                age = randrange(31),
                sex = choice(['muj', 'jena']),
                group = randrange(10),
                faculty_id = i
            )
            db.session.add(studen)
    db.session.commit()
    print(f'данные добавлены')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        add_user()
    app.run(debug=True)
