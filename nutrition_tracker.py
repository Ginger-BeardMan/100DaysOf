import requests
from datetime import datetime

DATE = datetime.now()
TIME = datetime.time(DATE)

current_date = str(DATE.strftime("%m/%d/%Y"))
current_time = str(TIME.strftime('%-H:%-M:%S'))

# ------------------------------------------------- NutritionIX API -------------------------------------------------
APP_ID = # YOUR APP_ID

API_KEY = # YOUR API_KEY

GENDER = # YOUR GENDER
WEIGHT_KG = # YOUR WEIGHT IN KG
HEIGHT_CM = # YOUR HEIGHT IN CM
AGE = # YOUR AGE IN YEARS

exercise_stats_endpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'

exercise_input = input('Tell me which exercise you did: ')

exercise_headers = {
    'x-app-id': APP_ID,
    'x-app-key': API_KEY,
    'Content-Type': 'application/json'
}

exercise_config = {
    "query": exercise_input,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}

nutrition_response = requests.post(exercise_stats_endpoint, headers=exercise_headers, json=exercise_config)
nutrition_response.raise_for_status()
nutrition_result = nutrition_response.json()['exercises'][0]

exercise = str(nutrition_result['user_input'])
duration = str(nutrition_result['duration_min'])
calories = str(nutrition_result['nf_calories'])

# --------------------------------------------------- Sheety API ---------------------------------------------------

BEARER_TOKEN = # YOUR BEARER TOKEN

sheety_workouts_endpoint = # YOUR SHEETY API ENDPOINT

sheety_config = {
    'workout': {
        'date': current_date,
        'time': current_time,
        'exercise': exercise,
        'duration': duration,
        'calories': calories,
    }
}

header = {
    "Authorization": f'Bearer {BEARER_TOKEN}'
}

sheety_response = requests.post(sheety_workouts_endpoint, json=sheety_config, headers=header)
sheety_response.raise_for_status()
