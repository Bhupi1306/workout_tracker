from pydantic import BaseModel, EmailStr
from enum import Enum


#-----ENUMS-----#

class ExerciseCat(str, Enum):
    Flexibility = 'Flexibility'
    Strength = 'Strength'
    Cardio = 'Cardio'


    
class MuscleGroup(str, Enum):
    Chest = 'Chest'
    Back = 'Back'
    Shouler = 'Shoulder'
    Arm = 'Arm'
    Core = 'Core'
    Leg = 'leg'

class TokenType(str, Enum):
    access = 'access'
    refresh = 'refresh'


#-----USER-----#

class UserLogin(BaseModel):
    email:EmailStr
    password: str

class User(BaseModel):
    user_name : str
    email: EmailStr

class UserCreate(User):
    password: str

class UserOut(User):
    id: int
    token: str | None = None

    class Config:
        from_attributes=True



#-----EXERCISE-----#



class ExerciseCreate(BaseModel):
    name : str
    description : str
    category : ExerciseCat
    muscle_group: MuscleGroup

class ExerciseOut(ExerciseCreate):
    id: int

    class Config:
        from_attributes=True


#-----WORKOUT PLAN-----#

class WorkoutPlanCreate(BaseModel):
    name: str

    class Config:
        from_attributes=True



#-----WORKOUT EXERCISES-----#

class WorkoutExercise(BaseModel):
    exercise_id: int
    workout_plan_id: int
    completed: bool=False
    class Config:
        from_attributes=True