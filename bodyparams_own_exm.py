from fastapi import FastAPI,Body
from pydantic import BaseModel,Field,Required

class student(BaseModel):
    name:str|None = Field(default=Required,max_length=10,example='supriya')
    college:str|None = Field(default='Roiland',max_length=20,min_length=7,example='subha')
    age:int|None = Field(default=10,gt=20)
    daysAlive:float = Field(...,lt=10,gt=40)
    friends:list
    is_married:bool

app = FastAPI()

@app.get('/')
def getField():
    return {
        "hello" : "miss subhalaxmi"
    }
@app.post('/example')
def example(student:student):
    return {
        "data" :student
    }
    