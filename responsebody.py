from fastapi import FastAPI
from pydantic import BaseModel,EmailStr

app = FastAPI()

class userIn(BaseModel):
    username:str
    password:str
    email:EmailStr
    full_name:str | None = None

class UserOut(BaseModel):
    username:str
    email:EmailStr
    full_name:str | None = None

class userInDB(BaseModel):
    username:str
    hashed_password:str
    email:EmailStr
    full_name:str | None = None

def fake_password_hasher(raw_password :str):
    return "supersecret" + raw_password

def fake_save_user(user_in:userIn):
    hashed_password = fake_password_hasher(user_in.password)
    user_in_db = userInDB(**user_in.dict(),hashed_password=hashed_password)
    print("user saved! ..not really")
    return user_in_db

def subhalaxmi(**values):
    print(values)

subhalaxmi(name="sup",age=20)

@app.post('/user')
def createUser(user: userIn):
    user_saved = fake_save_user(user)
    return user_saved
    
@app.get('/')
def getData():
    return {
        "hello":"hello subhalaxmi"
    }