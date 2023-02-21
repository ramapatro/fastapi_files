from fastapi import FastAPI,Form

app = FastAPI()
@app.get('/')
def getUser():
    return {
        "hello":"hii nanu"
    }

@app.post("/login/")
async def login(username:str = Form(),password:str = Form()):
    return {
        "username":username,
        "password":password
    }