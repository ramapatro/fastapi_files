from fastapi import FastAPI

app = FastAPI()
@app.get('/')
def homepage():
    li = []
    for i in range(1,100):
        li.append({
            "name":f'name - {i+1}',
            "age" :  f'age - {i*10}'
        })
    return {
        "message":"success",
        "status":200,
        "data":li
    }    

        