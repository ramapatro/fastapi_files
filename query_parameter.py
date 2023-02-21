from fastapi import FastAPI

app = FastAPI()
fake_items_db:list = [{"item_name":"food"},{"item_name":"drink"}]

#this is the normal path
@app.get('/')
def getAllUsers():
    return{
        "helllo":"world"
    }

#path params
@app.get('/user/{username}')
def shoeUser(username):
    return{
        "user":username
    }

#query params
@app.get('/user/')
def showUser(skip:int = 0,limit:int = 10):
    return fake_items_db[skip:skip + limit]

@app.get("/item/{item_id}")
async def read_item(item_id:str ,q:int):
    if q:
        return {"item_id":item_id,"q":q}
    return{"item_id":item_id}
