from fastapi import FastAPI
from enum import Enum
from pydantic import BaseModel

app = FastAPI()

class Tags(Enum):
    AHAN = 'ahannn'

class item(BaseModel):
    name:str
    description:str | None = None
    price : float
    tax : float |None = None
    Tags:set[str] = set()

@app.get('/',)
def getData():
    return {
        "hello":"come to the party subhalaxmi"
    }
@app.get('/1',tags=['nanu pilu'])
def getData1():
    return {
        "hello":"nanu piluuuuu......."
    }
@app.get('/2',tags=[Tags.AHAN],summary='i am the cuttest one')
def getData2():
    return {
        "hello":"ahannnnn"
    }
@app.get('/3',tags=[Tags.AHAN],description='this is all about only ahan')
def getData3():
    return {
        "hello":"ahannnnn"
    }
@app.post('/4',tags=['sunu pila'],response_model=item,response_description="the item")
def getData4(item:item):
    """
    Create an item with all the information:

    - **name**: each item must have a name
    - **description**: a long description
    - **price**: required
    - **tax**: if the item doesn't have tax, you can omit this
    - **tags**: a set of unique tag strings for this item
    """
    return item