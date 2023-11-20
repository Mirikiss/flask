import logging
from fastapi import FastAPI

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

@app.post('/items')
async def create_item(item: Item):
    logger.info('Отработка Post запроса')
    return item