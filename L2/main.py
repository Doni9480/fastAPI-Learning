from fastapi import FastAPI, Depends
from schemas import CreateUser
from sqlalchemy.orm import Session
from db_settings import get_session
from models import User, Address


app = FastAPI()


@app.post("/")
async def create_user(user: CreateUser, session: Session = Depends(get_session)):
    for address in user.dump:
        addr = Address(user.model_dump())
    user_obj = User(
        name="spongebob",
        fullname="Spongebob Squarepants",
        addresses=[],
    )
    # sandy = User(
    #     name="sandy",
    #     fullname="Sandy Cheeks",
    #     addresses=[
    #         Address(email_address="sandy@sqlalchemy.org"),
    #         Address(email_address="sandy@squirrelpower.org"),
    #     ],
    # )
    # patrick = User(name="patrick", fullname="Patrick Star")
    # session.add_all([spongebob, sandy, patrick])


@app.get("/")
async def root():
    return {"message": "Hello World"}