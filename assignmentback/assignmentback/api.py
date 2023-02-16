from psycopg2 import _psycopg2
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from Models import person, restaurant, review

db_connection = psycopg2.connect(
database="python_assignment",
user="admin",
password="20MaximiLLiaN12",
host="localhost",
port= '5432'
)
cursor_obj = db_connection.cursor()

app = FastApi()

def populate_database():
    db_connection = psycopg2.connect(
database="python_assignment",
user="admin",
password="20MaximiLLiaN12",
host="localhost",
port= '5432'
)
cursor_obj = db_connection.cursor()
with cursor_obj.connection as cursor:
    cursor.execute(open("setupDB.sql", "r").read())
    cursor.close()
    cursor.connection.commit()
    cursor.connection.close()


@app.get("/", response_class=HTMLResponse)
def root():
    return "Hello World"

@app.get("/populateDb")
def root():
    populate_database
    return "populated database"



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

#Get review with id
@app.get("/review/{id}")
def get_review_by_id(id: int):
    data = db.get(table="review", where=("id", str(id)))
    return data

@app.post("/create_person")
def create_person(person: person):
    create_person_query = """INSERT INTO people (
        first_name, last_name,
        born, city, gender ) VALUES (
            ?,?,?,?,?)
            """ 
    db.call_db(create_person_query, person.first_name,person.last_name, person.born,
               person.city, person.gender)
    return person;