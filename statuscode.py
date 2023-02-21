from fastapi import FastAPI,status
from pydantic import BaseModel
from datetime import datetime

app= FastAPI()

class User(BaseModel):
    name:str
    age:int
    instagram_folloewrs:float
    is_married:bool
    friends:list[str]
    college:str

@app.get('/',status_code=status.HTTP_200_OK)
def getuser():
    return {
        "hello" :"hello subhalaxmi"
        }

@app.post('/user',status_code=status.HTTP_201_CREATED)
def getuser(user:User):
    if not user:
        return {
            "message":"failed",
            "status_code":status.HTTP_400_BAD_REQUEST,
            "update_at":datetime.now()
        }
    return {
         "message":"success",
        "status_code":status.HTTP_201_CREATED,
        "data":user,
        "update_at":datetime.now()
    }