from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def root():
    return {'massager': 'Hello world!!!'}

@app.get("/items/{iten_id}")
async def read_item(iten_id: int, q: str = None):
    return {"iten_id": iten_id, "q": q}