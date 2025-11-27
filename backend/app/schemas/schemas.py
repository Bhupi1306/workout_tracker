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





#-----USER-----#

class User(BaseModel):
    user_name : str
    email: EmailStr

class UserCreate(User):
    password: str

class UserOut(User):
    id: int

    class Config:
        orm_mode=True



#-----EXERCISE-----#



class ExerciseCreate(BaseModel):
    name : str
    description : str
    category : ExerciseCat
    muscle_group: MuscleGroup

class ExerciseOut(ExerciseCreate):
    id: int

    class Config:
        orm_mode=True


#-----WORKOUT PLAN-----#

class WorkoutPlanCreate(BaseModel):
    name: str
    user_id: int

class WorkoutPlanOut(BaseModel):
    id: int

    class Config():
        orm_mode=True



#-----WORKOUT EXERCISES-----#

class WorkoutExercise(BaseModel):
    exercise_id: int
    workout_plan_id: int
    completed: bool=False

class WorkoutExerciseOut(BaseModel):
    id: int

    class Config:
        orm_mode=True
