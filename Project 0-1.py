# Allowed list of vehicles
AllowedVehiclesList = ['Ford F-150', 'Chevrolet Silverado', 'Tesla Cybertruck', 'Toyota Tundra', 'Nissan Titan']

def display_menu():
     print("********************************")
     print("AutoCountry Vehicle Finder v0.1")
     print("********************************")
     print("Please Enter the following number below from the following menu:")
     print("1. PRINT all Authorized Vehicles")
     print("2. Exit")
 
 #If 1, print all authorized vehicles
def print_vehicles():
    print("The AutoCountry sales manager has authorized the purchase and selling of the following vehicles: ")
    for vehicle in AllowedVehiclesList:
        print(vehicle)
 
# Loop to display menu and get user input, if 2 then exit
while True: 
    display_menu()
    choice = input("Please enter your choice: ")
    if choice == '1':
        print_authorized_vehicles = print_vehicles()
    elif choice == '2':
        print("Thank you for using the AutoCountry Vehicle Finder, good-bye!")
        break