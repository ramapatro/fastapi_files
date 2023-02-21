from fastapi import FastAPI,Depends

app = FastAPI()
fake_items_db:list = [{"item_name":"sup"},{"item_name":"nanu"},{"item_name":"rinki"}]

#function level dependency
#def depending_fn(q:str | None = None, skip : int = 0 ,limit:int =100 ):
#return{"q":q,"skip":skip,"limit":limit}

# @app.get('/')
# async def getuser():
#     return {
#         "hello":"hii suppp"
#     }
# #query params
# @app.get('/user/')
# def showUser(skip:int = 0,limit:int = 10):
#     return fake_items_db[skip :skip + limit]

def depending_fn(skip : int = 0 ,limit:int =100 ):
    return fake_items_db[skip:skip +limit]
class DependingClass:
    def __init__(self,skip:int = 0 ,limit:int = 10 ) :
        self.skip = skip;
        self.limit = limit
@app.get('/')
async def getuser():
    return {
        "hello":"hii nanuuu"
    }
@app.get('/user/')
def showUser(depends:DependingClass = Depends(DependingClass)):
    return fake_items_db[depends.skip:depends.skip +depends.limit]