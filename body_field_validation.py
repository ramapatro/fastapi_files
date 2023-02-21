from fastapi import FastAPI,Body
from pydantic import BaseModel,Field

app = FastAPI()

@app.get('/')
def getReq():
    return {
        "hello" : "world"
    }
class BodyField(BaseModel):
    name:str
    description : str | None = Field(
        default=None,description='please enter here the description')
    currency:float | None = Field(default=None)

@app.post('/bodyData')
def getBodyData(profile:BodyField = Body(embed=True)):
    return {
        "body fields":profile
    }
    
# @app.post('/example')
# def example(student:student):
#     return {
#         "data":student
#     }