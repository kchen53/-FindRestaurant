import restaurants
import recipes

def main():

    print("What would you like to do?", end="\n")
    print("Stir or Dine is the question :)", end="\n\n")

    response = input("What would you like to eat?")

    print("Here are some recipe options in case you want to stay home!", end="\n")
    recipes.find_recipes(response)

    response += " in tampa, FL"
    print("Going out to eat is an option too!", end="\n")
    restaurants.find_restaurants(response)

main()







