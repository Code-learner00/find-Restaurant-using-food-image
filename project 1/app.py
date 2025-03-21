import json

# Load the JSON data from file1.json
with open('file1.json', 'r') as file:
    data = json.load(file)

def search_restaurants_by_food_item(food_item):
    """
    Search for restaurants that serve a specific food item.
    :param food_item: Name of the food item to search for.
    :return: List of restaurants where the food item is available.
    """
    restaurants = []
    
    # Iterate through the restaurants in the JSON data
    for restaurant in data[0]['restaurants']:
        menu_url = restaurant['restaurant']['menu_url']
        # Assuming the menu_url contains the food items (you may need to scrape the menu)
        # For now, we'll just check if the food item is in the restaurant's cuisines
        if food_item.lower() in restaurant['restaurant']['cuisines'].lower():
            restaurants.append(restaurant['restaurant']['name'])
    
    return restaurants

if __name__ == "__main__":
    # Example usage
    food_item = input("Enter the name of the food item: ")
    restaurants = search_restaurants_by_food_item(food_item)
    
    if restaurants:
        print(f"Restaurants serving {food_item}:")
        for restaurant in restaurants:
            print(f"- {restaurant}")
    else:
        print(f"No restaurants found serving {food_item}.")