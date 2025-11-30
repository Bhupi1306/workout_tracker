from fastapi import FastAPI, Depends, HTTPException

from app.db.connect import create_table
from app.routers import register

app = FastAPI()

create_table()

app.include_router(register.router)

@app.get("/")
async def root():
    return {"message": "Connected"}


