from .connect import Base
from sqlalchemy import Column, Integer, String, TIMESTAMP, Boolean, text, ForeignKey, ARRAY
from sqlalchemy.orm import relationship


# All models for database

class Exercise(Base):
    __tablename__ = "exercises"

    id = Column(Integer, primary_key=True, nullable=False, index = True)
    name = Column(String,nullable=False, index = True)
    description = Column(String,nullable=False)
    category = Column(ARRAY(String),nullable=False)
    muscle_group = Column(ARRAY(String),nullable=False)

    workout_exercises = relationship("WorkoutExercise", back_populates="exercise")


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, nullable=False, index = True)
    user_name = Column(String, nullable=False, index=True)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)

    workout_plans = relationship("WorkoutPlan", back_populates="user")
    


class WorkoutPlan(Base):
    __tablename__ = "workout_plans"

    id = Column(Integer, primary_key=True, nullable=False, index = True)
    name = Column(String, nullable=False)
    user_id = Column(Integer,ForeignKey("users.id"), nullable=False)
    
    user = relationship("User",  back_populates="workout_plans")
    workout_exercises = relationship("WorkoutExercise", back_populates="workout_plan")

class WorkoutExercise(Base):
    __tablename__ = "workout_exercises"

    id = Column(Integer, primary_key=True, nullable=False, index = True)
    exercise_id = Column(Integer, ForeignKey("exercises.id"),nullable=False)
    workout_plan_id = Column(Integer, ForeignKey("workout_plans.id"), nullable=False)
    completed = Column(Boolean, default=False)
    
    exercise = relationship("Exercise", back_populates="workout_exercises")
    workout_plan = relationship("WorkoutPlan", back_populates="workout_exercises")