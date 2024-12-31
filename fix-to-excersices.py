# Import necessary libraries
import json
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def load_exercises(file_path):
    with open(file_path, "r") as file:
        return json.load(file)

def fix_exercises(exercises):
    for exercise in exercises:
        exercise_id = exercise.get("id", "Unknown")
        
        # Fix empty secondaryMuscles
        if not exercise.get("secondaryMuscles") or exercise["secondaryMuscles"] == []:
            exercise["secondaryMuscles"] = ["None"]
            logger.info(f"Fixed empty secondaryMuscles for {exercise_id}")

        # Fix empty mechanic
        if not exercise.get("mechanic"):
            exercise["mechanic"] = "isolation"  # Default to isolation if unknown
            logger.info(f"Fixed empty mechanic for {exercise_id}")

        # Fix empty force
        if not exercise.get("force"):
            exercise["force"] = "push"  # Default to push if unknown
            logger.info(f"Fixed empty force for {exercise_id}")

        # Fix empty instructions
        if not exercise.get("instructions") or exercise["instructions"] == []:
            exercise["instructions"] = ["No instructions available"]
            logger.info(f"Fixed empty instructions for {exercise_id}")

    return exercises

def fix_empty_equipment(exercises):
    bodyweight_keywords = ['stretch', 'circles', 'lunge', 'bodyweight', 'pose', 'drill',
                         'bound', 'hops', 'climbers', 'push-up', 'squats', 'walking']
    
    fixed_count = 0
    for exercise in exercises:
        if not exercise.get("equipment") or exercise["equipment"] == "":
            # Check if it's a bodyweight exercise based on name
            name = exercise.get('name', '').lower()
            is_bodyweight = any(keyword in name.lower() for keyword in bodyweight_keywords)
            
            if is_bodyweight:
                exercise["equipment"] = "body only"
            else:
                exercise["equipment"] = "other"  # Default fallback
                
            fixed_count += 1
            logger.info(f"Fixed empty equipment for exercise: {exercise.get('id', 'Unknown')}")
    
    return exercises, fixed_count

def save_exercises(exercises, output_file):
    with open(output_file, 'w') as file:
        json.dump(exercises, file, indent=2)
    logger.info(f"Saved fixed exercises to {output_file}")

def main():
    input_file = "fixed_exercises_with_github_images.json"  # Replace with your input file path
    output_file = "fixed_exercises.json"
    
    exercises = load_exercises(input_file)
    fixed_exercises, count = fix_empty_equipment(exercises)
    fixed_exercises = fix_exercises(fixed_exercises)
    save_exercises(fixed_exercises, output_file)
    logger.info(f"Fixed equipment for {count} exercises")

if __name__ == "__main__":
    main()