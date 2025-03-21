from app import search_restaurants_by_food_item

def search_by_name():
    food_item = input("Enter the name of the food item: ")
    restaurants = search_restaurants_by_food_item(food_item)
    
    if restaurants:
        print(f"Restaurants serving {food_item}:")
        for restaurant in restaurants:
            print(f"- {restaurant}")
    else:
        print(f"No restaurants found serving {food_item}.")

if __name__ == "__main__":
    search_by_name()