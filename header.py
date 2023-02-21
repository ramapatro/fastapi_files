from fastapi import FastAPI,Header

app = FastAPI()
@app.get("/items/")
# async def read_items(user_agent:str | None = Header(default=None)):
#     return{
#         "User_agent":user_agent
#     }
#### async def read_items(method:str | None = Header(default=None)):
#     return{
#         "User_agent":method
#     }
async def read_items(x_token:str | None = Header(default=None),bearer_token:str|None = Header(default=None)):
    return{
        "x_token":x_token,"bearer_token":bearer_token
    }
