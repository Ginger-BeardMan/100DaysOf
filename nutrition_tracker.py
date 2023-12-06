import requests
from datetime import datetime
import os

DATE = datetime.now()
TIME = datetime.time(DATE)

current_date = str(DATE.strftime("%m/%d/%Y"))
current_time = str(TIME.strftime('%-H:%-M:%S'))

# ------------------------------------------------- NutritionIX API -------------------------------------------------

exercise_input = input('Tell me which exercise you did: ')

exercise_headers = {
    'x-app-id': os.environ['APP_ID'],
    'x-app-key': os.environ['API_KEY'],
    'Content-Type': 'application/json'
}

exercise_config = {
    "query": exercise_input,
    "gender": os.environ['GENDER'],
    "weight_kg": os.environ['WEIGHT_KG'],
    "height_cm": os.environ['HEIGHT_CM'],
    "age": os.environ['AGE'],
}
exercise_stats_endpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'

nutrition_response = requests.post(url=exercise_stats_endpoint, headers=exercise_headers, json=exercise_config)
nutrition_response.raise_for_status()
nutrition_result = nutrition_response.json()['exercises'][0]

exercise = str(nutrition_result['user_input'])
duration = str(nutrition_result['duration_min'])
calories = str(nutrition_result['nf_calories'])

# --------------------------------------------------- Sheety API ---------------------------------------------------

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
    "Authorization": f'Bearer {os.environ["BEARER_TOKEN"]}'
}

sheety_response = requests.post(url=os.environ['sheety_workouts_endpoint'], json=sheety_config, headers=header)
sheety_response.raise_for_status()

