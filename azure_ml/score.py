import json

def sleep_factor(hours):
    if 7 <= hours <= 8:
        return 1.0
    else:
        return max(0.5, 1 - abs(7.5 - hours) * 0.2)

current_growth = 100  # baseline, can be reset or persisted externally

def sleep_factor(hours):
    if 7 <= hours <= 8:
        return 1.0
    else:
        return max(0.5, 1 - abs(7.5 - hours) * 0.2)

current_growth = 100  # baseline, can be reset or persisted externally

def init():
    global current_growth
    current_growth=100

def run(input_data):
    global current_growth
    data=json.loads(input_data)
    training_intensity=data["training_intensity"]
    nutrition_score=data["nutrition_score"]
    sleep_hours=data["sleep_hours"]
    recovery_score=data["recovery_score"]

    daily_multiplier=(training_intensity*
                      nutrition_score*
                      sleep_factor(sleep_hours)*
                      recovery_score)
    
    plateau_effect=max(0.1, 1-(current_growth/2000))
    increment=current_growth*daily_multiplier*plateau_effect*0.1
    current_growth+=increment

    return {"predicted_muscle_growth": current_growth}