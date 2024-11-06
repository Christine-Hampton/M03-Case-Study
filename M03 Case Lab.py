# Christine Hampton 
# M03 Case Lab 11/5/24
# Description: This app will define both the Superclass "Vehicle" and the subclass "Automobile", and will use the get_car_info function and display_car_info function 
# to help users gather and display information about a car. 

# Define the Vehicle superclass
class Vehicle: 
    def __init__(self, Vehicle_type):
        self.Vehicle_type = Vehicle_type

# Define the Automobile subclass which inherits from Vehicle
class Automobile(Vehicle):
    def __init__(self, year, make, model, doors, roof):
        super().__init__('car')
        self.year = year
        self.make = make 
        self.model = model 
        self.doors = doors
        self.roof = roof 

# Function to get user input and create an Automobile object
def get_car_info():
    year = input("Enter the year: ")
    make = input("Enter the make: ")
    model = input("Enter the model: ")
    doors = input("Enter the number of doors (2 or 4): ")
    roof = input("Enter the type of roof (solid or sun-roof): ")

    # Create an Automobile object
    car = Automobile(year, make, model, doors, roof)
    return car 

# Function to display car information 
def display_car_info(car):
    print(f"Vehicle type: {car.Vehicle_type}")
    print(f"Year: {car.year}")
    print(f"Make: {car.make}")
    print(f"Model: {car.model}")
    print(f"Number of doors: {car.doors}")
    print(f"Type of roof: {car.roof}")

    # Main function to run the app
    def main():
        car = get_car_info()
        print("\nHere is the information about your car:")
        display_car_info(car)

    if __name__ == "__Main__":
        main()