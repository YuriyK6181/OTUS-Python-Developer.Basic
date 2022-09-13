"""
API - application programming interface
"""
from datetime import datetime

from fastapi import FastAPI

from pydantic import constr

from view import router as view_router

app = FastAPI()
app.include_router(view_router)


@app.get("/")
def root():
    return {"message": "Type ping after/!!"}


@app.get("/hello")
def hello(name: constr(min_length=3) = "OTUS"):
    return {"message": "Hello, "+name+'!', "now": datetime.now()}


@app.get("/ping")
def ping():
    return {"message": "pong"}


@app.get("/get_sym_code")
def get_sym_code(s: str):
    if len(s) > 1:
        s = s[1]
    return {"message": "Code for symbol '"+s+"' is "+str(ord(s))}


@app.get("/get_str_to_code")
def get_sym_code(s: str):
    res = []
    print(s)
    for ss in s:
        mes = "Symbol '"+ss+"'"
        cod = str(ord(ss))
        res.append(mes+":"+cod)
    return res


@app.get("/power")
def add_values(a: int, b: int):
    return {
        "a": a,
        "b": b,
        "power": a ** b,
    }
