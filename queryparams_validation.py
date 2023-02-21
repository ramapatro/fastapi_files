from fastapi import FastAPI,Query
app = FastAPI()

@app.get('/')
def homepage():
    return {
        "homepage"
    }
    
#query params validation
@app.get('/sup/')
def sup_validation(age:str):
    results = {"data":[{"name":'subhalaxmi patro'}]}
    if age:
        results.update({"age":age})
    return results 


@app.get('/family/')
def rinki_validation(member:str | None = Query(default=None,max_length=20)):
    results = {'data':[{"didi":'rinki'},{"tingiri":'ahan'}]}    
    if member:
        results.update({'important hauchi': member})
    return results

# @app.get('/family/')
# def rinki_validation(member:str | None = Query(max_length=20,min_length=10)):
#     results = {'data':[{"didi":'rinki'},{"tingiri":'ahan'}]}    
#     if member:
#         results.update({'important hauchi': member})
#     return results

@app.get('/family/')
def rinki_validation(member:str | None = Query(default=...,max_length=10)):
    results = {'data':[{"didi":'rinki'},{"tingiri":'ahan'}]}    
    if member:
        results.update({'important hauchi': member})
    return results

#mulitiple query parameters
@app.get('/nanu_boy')
def nanu_multi_validation(ahan:list[str] | None = Query(default=["chameli","hai"],
description='nanu is tingri good boy',
title='nanu kn karucha wa',
deprecated=True,
alias='btw aji kn khaila',
include_in_schema=False
)):
    return {
        "ahan":ahan
    }

