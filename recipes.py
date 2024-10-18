import requests
from dotenv import load_dotenv
import os

load_dotenv()

def find_recipes(prompt):
    items = {}
    api_key = os.getenv("RECI_API_KEY")
    url = "https://api.spoonacular.com/recipes/complexSearch"

    params = {
    "query": prompt,
    "apiKey": api_key,
    "addRecipeInformation": "true"
    }
    
    response = requests.get(url, params=params)

    if response.status_code == 200:
        for i, recipe in enumerate(response.json().get("results", [])):
            # print("Option:", i + 1, " title: ", recipe["title"], "URL: ", recipe["sourceUrl"])
            items[recipe["title"]] = [recipe["sourceUrl"]]
        return items
    else:
        print(response.status_code)

# find_recipes("pizza")

