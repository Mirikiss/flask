from fastapi import APIRouter
from model import User, UserIn
from db import users, database


router = APIRouter()

@router.get('/')
async def root():
    return 'hello'

@router.get('/users', response_model=list[User])
async def get_users():
    query = users.select
    return await database.fetch_all(query)

@router.get('/users/{user_id}', response_model=User)
async def one_user(user_id: int):
    query = users.select().where(users.c.id==user_id)
    return await database.fetch_one(query)

@router.post('/users/', response_model=User)
async def creat_user(user: UserIn):
    query = users.insert().value(name=user.name, email=user.email, password = user.password)
    await database.execute(query)
    return f'Пользователь добавлен'

@router.put('/users/{user_id}')
async def edit_user(user_id: int, new_user: UserIn):
    query = users.update(name=user.name, email=user.email, password = user.password)
    await database.execute(query)
    return f'Пользователь изменён'

@router.delete('/user/{user_id}')
async def del_open(user_id: int):
    query = users.delete().where(users.c.id == user_id)
    await database.execute(query)
    return 'удаление'