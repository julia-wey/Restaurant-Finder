# lib/helpers.py

from models.city import City
from models.restaurant import Restaurant

def exit_program():
    print("Goodbye!")
    exit()
    
def list_cities():
    cities = City.display_all()
    for city in cities:
        print(city)

def find_city_by_name():
    name = input("Enter the city's name: ")
    city = City.find_city_by_name(name)
    print(city) if city else print(f'{name} not found')

def find_city_by_id():
    id_ = input("Enter the city's id: ")
    city = City.find_by_id(id_)
    print(city) if city else print(f'City {id_} not found')

def create_city():
    name = input("Enter the city's name: ")
    state = input("Enter the city's state: ")
    try:
        city = City.create(name, state)
        print(f'City of {name} successfully added.')
    except Exception as exc:
        print('Error adding city: ', exc)

def delete_city():
    id_ = input("Enter the city's id: ")
    if city := City.find_by_id(id_):
        city.delete()
        print(f'City {id_} deleted.')
    else:
        print(f'City {id_} not found.')

def list_restaurants():
    restaurants = Restaurant.display_all()
    for restaurant in restaurants:
        print(restaurant)

def find_restaurant_by_name():
    name = input("Enter the restaurant's name: ")
    restaurant = Restaurant.find_restaurant_by_name(name)
    print(restaurant) if restaurant else print(f'{name} not found')

def find_restaurant_by_id():
    id_ = input("Enter the restaurant's id: ")
    restaurant = Restaurant.find_by_id(id_)
    print(restaurant) if restaurant else print(f'ID of {id_} not found')

def create_restaurant():
    name = input("Enter the restaurant's name: ")
    cuisine = input("Enter the restaurant's cuisine: ")
    city_id = input("Enter the restaurant's city id: ")
    try:
        restaurant = Restaurant.create(name, cuisine, city_id)
        print(f'{name} successfully added.')
    except Exception as exc:
        print('Error adding restaurant: ', exc)

def delete_restaurant():
    name = input("Enter the restaurant's name: ")
    if restaurant := Restaurant.find_restaurant_by_name(name):
        restaurant.delete()
    else:
        print(f'{name} not found.')

