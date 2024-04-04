# import du package fastapi
from fastapi import FastAPI, HTTPException
from models import User, Gender, Role
from uuid import uuid4, UUID
from typing import List

#initialisation de l'application
app = FastAPI()

db: List[User] = [

    User(

        id = uuid4(),
        first_name = "axel",
        last_name = "tifrani",
        gender = Gender.male,
        roles=[Role.admin, Role.user]
    ),

    User(

        id = uuid4(),
        first_name = "Toto",
        last_name = "titi",
        gender = Gender.male,
        roles=[Role.admin, Role.user]
    )
]

# Creation d'un methode get root
@app.get("/")
def root():
    return {"message" : "Page d'acceuil"}


# Creation d'un methode get home
@app.get("/home")
def home():
    return {"Salutation" : "Bonjour à tous"}

# Creation d'une methode get all users
@app.get("/api/v1/users")
def get_users():
    return db

# Creation d'une methode post new user
@app.post("/api/v1/user")
def add_users(user:User):
    db.append(user)
    return 'User succesfully added'

# Creation d'une methode get d'un user par id
@app.get("/api/v1/user/{id}")
def get_user(id:UUID):
    for user in db:
        if user.id == id:
            return user
       
    raise HTTPException(
        status_code= 404,
        detail= f"Error 404. User with id {id}, not found."
        )
