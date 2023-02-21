from fastapi import FastAPI,HTTPException,status,requests
import base64
from fastapi.responses import JSONResponse

app = FastAPI()

class customerror(Exception):
    def __init__(self,name: str) -> None:
        self.name = name

@app.get('/')
def getData():
    return {
        "hello":"hiii ahannnn"
    }

@app.exception_handler(customerror)
async def unicorn_exception_handler(request:requests,exc:customerror):
    return JSONResponse(
        status_code=400,
        content={'message':f"Oops! {exc.name} did something. there goes a rainbow..."}
    )

@app.exception_handler(customerror)
async def unicorn_exception_handler(request:requests,exc:customerror):
    return JSONResponse(
        status_code=status.HTTP_405_METHOD_NOT_ALLOWED,
        content={'message':f"{exc.name} is unauthorized"}
    )
#handling error
# @app.get('/user/{username}/{token}')
# def getuser(username:str,token:str):
#     if not token:
#         raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail='username is unouthorized',
#         headers={"token":"no token is provided"})
#     if username != 'subhalaxmi':
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='username is invalid',
#         headers={"name":"nanu is subhaa's boy"})
#     return {
#         "user":username,
#         "token":token
#        # "token":base64.b64decode(token)
#     }

@app.get('/user/{username}/{token}')
def getuser(username:str,token:str):
    if not token:
        raise customerror(name=username)
    if username != 'subhalaxmi':
        raise customerror(name=token)
    return {
        "user":username,
        "token":token
       # "token":base64.b64decode(token)
    }