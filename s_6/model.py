from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    emal:str

class UserIn(BaseModel):
    name: str
    emal:str
    password: str