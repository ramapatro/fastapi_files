from fastapi import FastAPI,Request
from pydantic import BaseModel

class nanu(BaseModel):
    name:str;
    age:int;
    nick_namw:str;

app = FastAPI()

@app.get('/user')
def family(req:Request):
    return {
        "baseURL":req._base_url,
        "method":req.method,
        "host":req.headers
    }
