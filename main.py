import requests
from dotenv import load_dotenv
import os

load_dotenv()

def find_restaurants(prompt):
    api_key = os.getenv("YOUR_API_KEY")
    url = "https://maps.googleapis.com/maps/api/place/textsearch/json"

    params = {
    "query": prompt,
    "inputtype": "textquery",
    "key": api_key
    }
    
    response = requests.get(url, params=params)

    if response.status_code == 200:
        # return response.json()
        results = response.json().get("results", [])
        for place in results:
            if place["rating"] > 4.5:
                print("Name: ", place["name"], "Address: ", place["formatted_address"], "Business Status: ", place["business_status"])
    else:
        print("Nothing")

find_restaurants("pizza in Tampa, FL")

