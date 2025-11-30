from fastapi import FastAPI, Depends, HTTPException

from app.db.connect import create_table

from app.routers import register
from app.routers import login
from app.routers import refresh

app = FastAPI()

create_table()

app.include_router(register.router)
app.include_router(login.router)
app.include_router(refresh.router)

@app.get("/")
async def root():
    return {"message": "Connected"}


