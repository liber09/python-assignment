from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from Models import person, restaurant, review

@app.get("/", response_class=HTMLResponse)
def root():
    with open("index.html") as f:
        return f.read()

#Get person with id
@app.get("/persons/{id}")
def get_person_by_id(id: int):
    data = db.get(table="person", where=("id", str(id)))
    return data

#Get Restaurant with id
@app.get("/restaurant/{id}")
def get_restaurant_by_id(id: int):
    data = db.get(table="restaurant", where=("id", str(id)))
    return data

#Get person with id
@app.get("/reviuew/{id}")
def get_review_by_id(id: int):
    data = db.get(table="review", where=("id", str(id)))
    return data