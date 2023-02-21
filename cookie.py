from fastapi import FastAPI,Cookie

app = FastAPI()
@app.get('/')
def home():
    return {
        "home":"come home rightnow subu"
    }

@app.get('/cook')
def home(ads_id:str | None = Cookie(default=None)):
    return {
        "home":ads_id
    }