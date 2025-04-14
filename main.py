from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
import os
import uvicorn

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

origins = [
    "http://localhost:3000", # Your React frontend development server
    # Add your deployed Vercel frontend URL here when you have it, e.g.:
    "https://vitality-vista.vercel.app",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins, # List of origins that are allowed to make requests
    allow_credentials=True, # Allow cookies to be included in requests (optional)
    allow_methods=["*"], # Allow all standard methods (GET, POST, etc.)
    allow_headers=["*"], # Allow all headers
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
    id: int
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
def get_exercise_by_id(exercise_id: int):
    """Fetch a single exercise by ID."""
    try:
        exercise_id = int(exercise_id)
        for exercise in exercise_data:
            if int(exercise["id"]) == exercise_id:
                return exercise
        raise HTTPException(status_code=404, detail="Exercise not found")
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid ID format")

@app.get("/exercises/search/{name}", response_model=List[Exercise], tags=["Exercises"])
def search_exercises_by_name(name: str):
    """Search exercises by name."""
    search_term = name.lower()
    matching_exercises = [
        exercise for exercise in exercise_data 
        if search_term in exercise["name"].lower()
    ]
    if not matching_exercises:
        return []
    return matching_exercises

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
