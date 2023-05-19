import requests
from datetime import datetime
import os


todays_date = datetime.today().strftime("%Y%m%d")
now_time = datetime.now().strftime("%X")

user_input = input("What exercises did you do today? ")

APP_ID = os.environ["APP_ID"]
API_KEY = os.environ["API_KEY"]
sheety_username = os.environ["sheety_username"]
NIX_TOKEN = os.environ['NIX_TOKEN']

nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = f"https://api.sheety.co/{os.environ.get('sheety_username')}/myWorkouts/workouts"

# Replace the code below with your own information
GENDER = ""
WEIGHT_KG = 00
HEIGHT_CM = 00
AGE = 00

headers = {
    "x-app-id": os.environ.get("APP_ID"),
    "x-app-key": os.environ.get("API_KEY"),
    "Content-Type": "application/json",
    "Authorization": os.environ.get("NIX_TOKEN")
}

nutritionix_params = {
    "query": user_input,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(url=nutritionix_endpoint, json=nutritionix_params, headers=headers)
result = response.json()
print(result)

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": todays_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(sheety_endpoint, json=sheet_inputs)

    print(sheet_response.text)