from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from db.connect import create_table, get_db
from db.models import User
from schemas.schemas import UserCreate

app = FastAPI()

create_table()

@app.get("/")
async def root():
    return {"message": "Connected"}

@app.post('/register')
async def login(user: UserCreate, db: Session = Depends(get_db)):

    if not user.user_name or not user.password or not user.email:
        raise HTTPException(status_code=400, detail="All fields are required")
        
    try:
        db_user = User(
            user_name=user.user_name,
            email=user.email,
            password=user.password
        )
        db.add(db_user)
        db.commit()
        db.refresh(db_user)


    except Exception as error:
        raise HTTPException(status_code=500, detail=error)
        
    return db_user