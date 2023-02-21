from fastapi import FastAPI,Response
from  fastapi.responses import RedirectResponse ,JSONResponse
from pydantic import BaseModel

app = FastAPI()

class item(BaseModel):
    name:str
    description:str | None = None
    price:float
    tax :float |None = None

# @app.get('/')
# def getData(item :item) -> item:
#     return [
#         item(name="mercidies", price= 2000000),
#         item(name= "audi" ,price= 100000000),
#     ]

@app.get("/portal")
async def get_portal(teleport:bool = False)-> Response:
    if teleport:
        return RedirectResponse(url="https://youtu.be/HL263brH-p0")
    return JSONResponse (content={"message":"here's your interdimentional portal.","status_code":200})