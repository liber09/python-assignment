from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from Models import person, restaurant, review

@app.get("/", response_class=HTMLResponse)
def root():
    with open("index.html") as f:
        return f.read()

@app.get("/persons/{id}")
def get_person_by_id(id: int):
    data = db.get(table="person", where=("id", str(id)))
    return data