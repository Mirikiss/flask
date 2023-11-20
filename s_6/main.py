from fastapi import FastAPI
import user
import uvicorn
from db import database

app = FastAPI()

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()
@app.include_router(user.router, tags=['Users'])
async def till():
    await 'sdad'

if __name__=='__main__':
    uvicorn.run('main:app', host='127.0.0.1', port=8000, reload=True)