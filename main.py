# import du package fastapi
from fastapi import FastAPI
from models import User, Gender, Role
from uuid import uuid4
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

# Creation d'une methode get users
@app.get("/api/v1/users")
def get_users():
    return db