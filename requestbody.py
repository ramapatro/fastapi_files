#import datetime
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class jeo(BaseModel):
    firstname :str
    lastname : str
    #date: datetime
    #diagonsed: bool

# @app.get('/')
# def getHome():
#      return{
#         "home":"page"
#      }

@app.post('/user')
def creo(user:jeo):
    return {
        "message":"user created successfully!",
        "status_code":201,
        "data":user,
        #"createdAt":"datetime.data(2023,2,3)"
    }