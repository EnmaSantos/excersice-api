from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

# Sample Exercise Data
import json

with open("fixed_exercises.json", "r") as file:
    exercise_data = json.load(file)

# FastAPI app initialization
app = FastAPI(
    title="Exercise API",
    description="API to fetch exercises and calorie burn information",
    version="1.0.0"
)

# Exercise Model
class Exercise(BaseModel):
    name: str
    force: str
    level: str
    mechanic: str
    equipment: str
    primaryMuscles: List[str]
    secondaryMuscles: List[str]
    instructions: List[str]
    category: str
    images: List[str]
    id: str
    calories_per_hour: int
    duration_minutes: int
    total_calories: float

# API Endpoints
@app.get("/", tags=["Root"])
def read_root():
    return {"message": "Welcome to the Exercise API!"}

@app.get("/exercises", response_model=List[Exercise], tags=["Exercises"])
def get_exercises():
    """Fetch all exercises."""
    return exercise_data

@app.get("/exercises/{exercise_id}", response_model=Exercise, tags=["Exercises"])
def get_exercise_by_id(exercise_id: str):
    """Fetch a single exercise by ID."""
    for exercise in exercise_data:
        if exercise["id"] == exercise_id:
            return exercise
    return {"error": "Exercise not found"}

import uvicorn

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000)
