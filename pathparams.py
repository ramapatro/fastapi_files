
from fastapi import FastAPI
from enum import Enum

class Modelname(str,Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

app = FastAPI()
@app.get("/users")
def getusers():
    return [
    {   "name":"subhalaxmi",
        "age":20
    } ,
    {
         "name":"rinki",
         "age":25
    }
    ]

@app.get('/users/{username}/{age}')
def getusers(username:str,age:int):
    return {
        "name":username ,
        "age":age
    }

# @app.get("/models/{model_name}")
# async def get_model(model_name:Modelname):
#     if model_name is Modelname.alexnet:
#         return {"model_name": model_name,"message":"Deep Learning FTW!"}
#     if model_name.value == "lenet":
#         return {"model_name":model_name, "message":"LeCNN all the images"}
#     return{"model_name":model_name,"message":"Have some residuals"}