def generate_workout_plan(user_profile):
    """
    Generate a simple progressive overload workout plan.
    
    user_profile: dict with keys:
        - fitness_level: 'beginner', 'intermediate', or 'advanced'
        - goal: 'muscle_gain', 'strength', or 'endurance'
        - available_days: number of training days per week (int)
    
    Returns:
        dict: workout plan with days as keys and list of exercises as values
    """
    base_plan = {
        'muscle_gain': ['Squats', 'Bench Press', 'Deadlift', 'Overhead Press', 'Rows'],
        'strength': ['Heavy Squats', 'Heavy Bench Press', 'Heavy Deadlift'],
        'endurance': ['Bodyweight Squats', 'Push-ups', 'Light Deadlifts', 'Planks']
    }
    
    fitness_modifiers = {
        'beginner': 1,
        'intermediate': 2,
        'advanced': 3
    }
    
    exercises = base_plan.get(user_profile.get('goal', 'muscle_gain'), base_plan['muscle_gain'])
    intensity = fitness_modifiers.get(user_profile.get('fitness_level', 'beginner'), 1)
    days = user_profile.get('available_days', 3)
    
    plan = {}
    for day in range(1, days + 1):
        # Assign exercises evenly across days, scaled by intensity
        day_exercises = []
        for i in range(intensity):
            exercise = exercises[(day - 1 + i) % len(exercises)]
            day_exercises.append(exercise)
        plan[f'Day {day}'] = day_exercises
    
    return plan

# Example usage
if __name__ == "__main__":
    user = {
        'fitness_level': 'beginner',
        'goal': 'muscle_gain',
        'available_days': 3
    }
    workout_plan = generate_workout_plan(user)
    for day, exercises in workout_plan.items():
        print(f"{day}: {', '.join(exercises)}")