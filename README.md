from fastapi import FastAPI, HTTPException
import uvicorn
from pydantic import BaseModel
from fastapi.responses import HTMLResponse

app = FastAPI()


class User(BaseModel):
    id: int
    name: str
    email: str
    password: int

class UserInput(BaseModel):
    name: str
    email: str
    password: int


users = [
    User(id=1, name='Serg', email='serg@mail.ru', password=12345678),
    User(id=2, name='Sasha', email='sasha@mail.ru', password=87654321),
    User(id=3, name='Rich', email='rich@mail.ru', password=14785236)
]

@app.get('/users')
async def main():
    return users

@app.get('/users/{users_id}')
async def requst_main(users_id: int):
    return users[users_id-1]

@app.post('/users', response_model=list[User])
async def add_main(user: UserInput):
    user = User(
        id=len(users)+1,
        name=user.name,
        email=user.email,
        password=user.password
    )
    users.append(user)
    print('Файл загружен')
    return users

@app.put('/users/{user_id}', response_model=UserInput)
def update(user_id: int, new_user: User):
    for i in users:
        if i.id == user_id:
            i.name = new_user.name
            i.email = new_user.email
            i.password = new_user.password
            return i
    raise HTTPException(status_code=404, detail='Отсутствует файл')

@app.delete('/user/{user_id}', response_model=str)
async def delete_data(user_id: int, new_user: UserInput):
    for i in users:
        if i.id == user_id:
            users.remove(i)
            return 'Файл удалён'
    raise HTTPException(status_code=404, detail='Отсутствует файл')

@app.get("/", response_class=HTMLResponse)
async def read_root():
    return "<h1>Hello World</h1>"


if __name__ == '__main__':
    uvicorn.run('main:app', host="127.0.0.1", port=8000, reload=True)
