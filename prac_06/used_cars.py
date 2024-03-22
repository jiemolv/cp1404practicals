
from prac_06.car import Car


def main():
    """Demo test code to show how to use car class."""
    # Create a new Car object called "limo" initialized with 100 units of fuel
    limo = Car("limo", fuel=100)

    # Add 20 more units of fuel to this new car object using the add method
    limo.add_fuel(20)

    # Print the amount of fuel in the car
    print(f"Amount of fuel in the car is {limo.fuel}")

    # Attempt to drive the car 115 km using the drive method
    driven_distance = limo.drive(115)
    print(f"Distance driven: {driven_distance}")

    # Print the car object/s to ensure the __str__ method is working as expected
    print(limo)

    my_car = Car(180)
    my_car.drive(30)
    print(f"Car has fuel: {my_car.fuel}")
    print(my_car)


main()