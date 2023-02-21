from fastapi import FastAPI,Query,Path,Body
from pydantic import BaseModel

class mix(BaseModel):
    name:str
    age:int

app = FastAPI()
@app.get('/mix')
def getmixpath():
    return{
        "message":"is this correctly working"
    }

@app.get('/mix')
def postmix(data:mix):
    return{
        "data": data
    }

# body params
@app.post('/body')
def postmix(data:mix):
    return{
        "data":data
    }

# path,query params
@app.put('/put/{name}')
def putmix(*,
          name: str = Path(default=None),
          q: str = Query(default=None),
          b : mix
          ):
    # print(name)
    # print(q)
    # print(b)
    # return {
    #     "data":"hello world"
    return {
        "path":name,
        "q":q,
        "b":b
    }
    class FAMILY(BaseModel):
        member:str;
        cute_member:str;
        age:int
    class patro(BaseModel):
        smart_meber:str;
        best:str;
        age:int;
        whatBest:FAMILY
    @app.post('/body_nested')
    def bodyNested(bestintheworld:patro):
        return {
            "data":bestintheworld
        }
#alii type mix
class item(BaseModel):
    name:str
    description:str | None = None
    price:float
    tax:float | None = None
class User(BaseModel):
    username:str
    dull_name:str | None = None
@app.put("/items/{item_id}")
async def update_item (
    *,
    item_id:int,
    item:item,
    user:User,
    importance:int = Body(gt=0,embed=True),
    inhome: int = Body(lt=5),
    q : str | None =None
):
    results = {"item_id":item_id,"item":item,"user":user,"importance":importance,"inhome":inhome}
    if q:
        results.update({"q":q})
    return results
@app.put("/item/{item_id}")
async def update_item(item_id: int, item :item = Body(embed=True)):
    results = {"item_id":item_id,"item":item}
    return results

    
         
    

