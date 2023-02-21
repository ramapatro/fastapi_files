from fastapi import FastAPI,Path,Query,Request
from pydantic import Required

app = FastAPI()

@app.get('/')
def homepage(req:Request):
    print(req._query_params,'request object')
    return{
        "ki karucha tumi?"
    }

#simple path param
@app.get("/{path}")
def family(path):
    print({"path":path})
    return {
        "path":path
    }

#simple path apram with path close
@app.get("/path/{path}")
def familywithme(path:float | None = Path(default=None,description="nanu",lt=5,gt=2)):
    print({"path":path})
    return {
        "path":path
    }
    
@app.get("/path/{path}")
def familywithme(path:float | None = Path(default=None,description="nanu",ge=5,deprecated=True,include_in_schema=True)):
    print({"path":path})
    return {
        "path":path
    }


@app.get("/path/{path}")
def familywithme(q:str | None = Query(default='ahan',description="nanu"),
                path:int|None = Path(default=None,description="nanu",ge=2,le=5,deprecated=True,include_in_schema=True)):
    print({"path":path})
    if q:
        return{
            "query":q
        }
    return {
        "path":path
    }

@app.get("/req/{path}")
def familywithme(q:str | None = Query(default=Required,description="nanu"),
                path:int|None = Path(default=None,description="nanu kunu",ge=2,le=5,deprecated=True,include_in_schema=True)):
    print({"path":path})
    if q:
        return{
            #"query":q,
            "path": Path,
            "query5":Required._query_params
            
        }
    

