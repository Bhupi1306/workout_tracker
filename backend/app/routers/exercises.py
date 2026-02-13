from fastapi import APIRouter, Depends, HTTPException, Response
from sqlalchemy.orm import Session

from ..db.connect import get_db
from ..db.seeder import seed_exercises

router = APIRouter(
    prefix="/workouts/exercises",
    tags=["exercise"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)

@router.post('/test-data')
def create_test_data(response: Response,db:Session = Depends(get_db)):
    try:
        count = seed_exercises(db)
        return {"message": f"{count} excercises created"}
    
    except Exception as error:
        print(error)
        raise HTTPException(status_code=500, detail="Something went wrong")



