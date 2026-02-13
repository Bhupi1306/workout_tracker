from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from typing import Annotated

from ..db.connect import get_db
from ..db.models import WorkoutPlan
from ..schemas.schemas import WorkoutPlanCreate, UserOut
from ..utils.get_current_user import get_current_user

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

router = APIRouter(
    prefix="/workouts",
    tags=["workouts"],
)

@router.post('/create', response_model=WorkoutPlanCreate)
def login(user: Annotated[UserOut, Depends(get_current_user)] ,workout_plan: WorkoutPlanCreate, db: Session = Depends(get_db)):

    try:
        # first check if exercise already exists in db
        db_workout_plan = db.query(WorkoutPlan).filter(
            WorkoutPlan.name == workout_plan.name,
            WorkoutPlan.user_id == user['id']
            ).first()
        if db_workout_plan:
            raise HTTPException(status_code=400, detail="Workout plan already exists")
        
        add_workout_plan = workout_plan.model_dump()
        add_workout_plan['user_id'] = user['id'] 
        added_workout_plan = WorkoutPlan(**add_workout_plan)

        db.add(added_workout_plan)
        db.commit()
        db.refresh(added_workout_plan)
        return added_workout_plan

        
    
    except HTTPException as http_error:
        raise http_error
    
    except Exception as error:
        print(error)
        raise HTTPException(status_code=500, detail="Something went wrong")
