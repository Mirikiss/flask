from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


@app.get('/')
async def reoad():
    logger.info('отработал гет запрос')
    return 'Hello world!!!'

@app.post("/items/")
async def create_item(item: Item):
    logger.info('Отработал POST запрос.')
    return item