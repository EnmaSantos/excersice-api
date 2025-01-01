import json

def update_exercise_ids():
    # Read existing exercises
    with open("fixed_exercises.json", "r") as file:
        exercises = json.load(file)
    
    # Update IDs sequentially
    for index, exercise in enumerate(exercises, start=1):
        exercise["id"] = str(index)
    
    # Save updated exercises
    with open("fixed_exercises.json", "w") as file:
        json.dump(exercises, file, indent=4)

if __name__ == "__main__":
    update_exercise_ids()
    print("Exercise IDs updated successfully!")