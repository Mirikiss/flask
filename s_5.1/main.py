from fastapi import FastAPI, HTTPException
import uvicorn
from typing import Optional
from pydantic import BaseModel
import logging

app = FastAPI()

class Task(BaseModel):
    id: int
    title: str
    description: Optional[str]
    status: bool

class TaskInput(BaseModel):
    title: str
    description: Optional[str]
    status: bool

tasks = [
    Task(id=1, title='1', description='1', status=True)
]

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/tasks")
async def get_tasks():
    return tasks



@app.post("/tasks", response_model=list[Task])
async def new_task(task: TaskInput):
    task = Task(
        id=len(tasks) + 1,
        title=task.title,
        description=task.description,
        status=task.status
    )
    tasks.append(task)
    return tasks

@app.get('/tasks/{task_id}', response_model=Task)
async def first_task(task_id: int):
    if len(tasks) < task_id:
        raise HTTPException(status_code=404, detail="Task not found")
    return tasks[task_id-1]


@app.put("/tasks/{task_id}", response_model=Task)
def edit_task(task_id: int, new_task: TaskInput):
    for task in tasks:
        if task.id == task_id:
            task.title = new_task.title
            task.description = new_task.description
            task.status = new_task.status
            return task
    raise HTTPException(status_code=404, detail="Task not found")

@app.delete("/tasks/{task_id}", response_model=str)
def edit_task(task_id: int, new_task: TaskInput):
    for task in tasks:
        if task.id == task_id:
            tasks.remove(task)        
            return f'Задача удалена'
    raise HTTPException(status_code=404, detail="Task not found")

class Genre(BaseModel):
    id:int
    title: str

class Movie(BaseModel):
    id: int
    title: str
    description: Optional[str]
    genre: Genre

movies = [Movie(id=1, title='Terminator', discription='film about ...', genre=Genre(id=1, title='фантастика')),
          Movie(id=2, title='Avatar', discription='film about ...', genre=Genre(id=2, title='comedia'))]

@app.get('/films', response_model=list[Movie])
async def get_genre(id_genre: int):
    my_movies = [i for i in movies if i.genre.id == id_genre]


if __name__ == '__main__':
    uvicorn.run('main:app', host="127.0.0.1", port=8000, reload=True)