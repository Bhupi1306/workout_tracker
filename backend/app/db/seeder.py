from sqlalchemy.orm import Session
from .models import Exercise



EXERCISES = [
    {
        "name": "Push Up",
        "description": "Bodyweight push exercise for upper body strength",
        "category": ["strength", "bodyweight"],
        "muscle_group": ["chest", "triceps", "shoulders"],
    },
    {
        "name": "Squat",
        "description": "Lower body compound movement",
        "category": ["strength"],
        "muscle_group": ["quadriceps", "glutes", "hamstrings"],
    },
    {
        "name": "Plank",
        "description": "Core stabilization exercise",
        "category": ["core", "bodyweight"],
        "muscle_group": ["abs", "shoulders"],
    },
]

def seed_exercises(db: Session):
    created = 0

    for exercise_data in EXERCISES:
        existing = db.query(Exercise).filter(
            Exercise.name == exercise_data["name"]
        ).first()

        if not existing:
            exercise = Exercise(**exercise_data)
            db.add(exercise)
            created += 1

    db.commit()

    return created
