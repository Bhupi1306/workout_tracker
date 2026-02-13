from fastapi import FastAPI, Depends, HTTPException

from app.db.connect import create_table

from app.routers import register
from app.routers import login
from app.routers import refresh
from app.routers import exercises
from app.routers import workouts

app = FastAPI()

create_table()

app.include_router(register.router, prefix="/api")
app.include_router(login.router, prefix="/api")
app.include_router(refresh.router, prefix="/api")
app.include_router(exercises.router, prefix="/api")
app.include_router(workouts.router, prefix="/api")

@app.get("/")
async def root():
    return {"message": "Connected"}


