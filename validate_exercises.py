# Import necessary libraries
import json

# Sample Exercise Data
import json

with open("fixed_exercises_with_github_images.json", "r") as file:
    exercise_data = json.load(file)

# Load the JSON file
def load_exercises(file_path):
    with open(file_path, "r") as file:
        return json.load(file)

# Check for missing or empty fields in each exercise
def find_invalid_exercises(exercises):
    invalid_exercises = []
    required_fields = [
        "name", "force", "level", "mechanic", "equipment",
        "primaryMuscles", "secondaryMuscles", "instructions",
        "category", "images", "id", "calories_per_hour",
        "duration_minutes", "total_calories"
    ]

    for exercise in exercises:
        errors = {}
        for field in required_fields:
            if field not in exercise:
                errors[field] = "Missing"
            elif not exercise[field]:
                errors[field] = "Empty"

        if errors:
            invalid_exercises.append({"id": exercise.get("id", "Unknown"), "errors": errors})

    return invalid_exercises

# Main function to load and validate exercises
def main():
    file_path = "fixed_exercises.json"  # Update with your file path
    exercises = load_exercises(file_path)
    
    invalid_exercises = find_invalid_exercises(exercises)

    if invalid_exercises:
        print("Invalid exercises found:")
        for entry in invalid_exercises:
            print(f"Exercise ID: {entry['id']}, Errors: {entry['errors']}")
    else:
        print("All exercises are valid!")

if __name__ == "__main__":
    main()