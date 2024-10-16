import requests
from dotenv import load_dotenv
import os

load_dotenv()

def find_recipes(prompt):
    api_key = os.getenv("RECI_API_KEY")
    url = "https://api.spoonacular.com/recipes/complexSearch"

    params = {
    "query": prompt,
    "apiKey": api_key,
    "addRecipeInformation": "true"
    }
    
    response = requests.get(url, params=params)

    if response.status_code == 200:
        for recipe in response.json().get("results", []):
            print("title: ", recipe["title"], "URL: ", recipe["sourceUrl"])
    else:
        print(response.status_code)

find_recipes("pizza")

