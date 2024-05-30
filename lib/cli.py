# lib/cli.py

from helpers import (
    exit_program,
    list_cities,
    find_city_by_name,
    find_city_by_id,
    create_city,
    delete_city,
    list_restaurants,
    find_restaurant_by_name,
    find_restaurant_by_id,
    create_restaurant,
    delete_restaurant
)

def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            list_cities()
        elif choice == "2":
            find_city_by_name()
        elif choice == "3":
            find_city_by_id()
        elif choice == "4":
            create_city()
        elif choice == "5":
            delete_city()
        elif choice == "6":
            list_restaurants()
        elif choice == "7":
            find_restaurant_by_name()
        elif choice == "8":
            find_restaurant_by_id()
        elif choice == "9":
            create_restaurant()
        elif choice == "10":
            delete_restaurant()
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit the program.")
    print("1. List all cities.")
    print("2. Find city by name.")
    print("3. Find city by id.")
    print("4. Add new city.")
    print("5. Delete city.")
    print("6. List all restaurants.")
    print("7. Find restaurant by name.")
    print("8. Find restaurant by id.")
    print("9. Add new restaurant.")
    print("10. Delete restaurant.")

if __name__ == "__main__":
    main()
