import os

def menu_print_vehicles():
    print_vehicles()

def menu_search_vehicle():
    vehicle_name = input("Please Enter the full vehicle name: ")
    search_vehicle(vehicle_name)

def menu_add_vehicle():
    add_vehicle()

def menu_delete_vehicle():
    delete_vehicle()
def display_menu():
    print("********************************")
    print("AutoCountry Vehicle Finder v0.1")
    print("********************************")
    print("Please Enter the following number below from the following menu:")
    print("1. PRINT all Authorized Vehicles")
    print("2. SEARCH for Authorized Vehicle")
    print("3. ADD Authorized Vehicle")
    print("4. DELETE Authorized Vehicle")
    print("5. Exit")
# Load the list of authorized vehicles from a file

file_path = "authorized_vehicles.txt"

def load_vehicles():
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            return [line.strip() for line in file.readlines()]
    else:
        return []

def save_vehicles():
    with open(file_path, "w") as file:
        for vehicle in AllowedVehiclesList:
            file.write(vehicle + "\n")

# Initialize the AllowedVehiclesList from the file
AllowedVehiclesList = load_vehicles()

# If 1, print all authorized vehicles
def print_vehicles():
    print("The AutoCountry sales manager has authorized the purchase and selling of the following vehicles: ")
    for vehicle in AllowedVehiclesList:
        print(vehicle)
#If 2, search for a vehicle
def search_vehicle(vehicle_name):
    if vehicle_name in AllowedVehiclesList:
        print(f"{vehicle_name} is an authorized vehicle.")
    else:
        print(f"{vehicle_name} is not an authorized vehicle, if you received this in error please check the spelling and try again.")
#If 3, add a vehicle
def add_vehicle():
    new_vehicle = input("Please Enter the full vehicle name you would like to add: ")
    if new_vehicle not in AllowedVehiclesList:
        AllowedVehiclesList.append(new_vehicle)
        print(f"You have added '{new_vehicle}' as an authorized vehicle.")
        save_vehicles()
    else:
        print(f"{new_vehicle} is already an authorized vehicle.")
#if 4, delete a vehicle
def delete_vehicle():
    vehicle_name = input("Please Enter the full Vehicle name you would like to REMOVE: ")
    if vehicle_name in AllowedVehiclesList:
        confirmation = input(f"Are you sure you want to remove '{vehicle_name}' from the Authorized Vehicles List?: ")
        if confirmation.lower() == 'yes':
            AllowedVehiclesList.remove(vehicle_name)
            print(f"You have REMOVED '{vehicle_name}' as an authorized vehicle.")
            save_vehicles()
    else:
        print(f"{vehicle_name} is not an authorized vehicle, if you received this in error please check the spelling and try again.")
#Loop to display menu and get user input, if 5 then exit
while True: 
    display_menu()
    choice = input("Please enter your choice: ")
    if choice == '1':
        print_authorized_vehicles = print_vehicles()
    elif choice == '2':
        vehicle_name = input("Please Enter the full vehicle name: ")
        search_vehicle(vehicle_name)
    elif choice == '3':
        add_vehicle()
    elif choice == '4':
        delete_vehicle()
    elif choice == '5':
        print("Thank you for using the AutoCountry Vehicle Finder, good-bye!")
        break
    else:
        print("Invalid choice. Please try again.")