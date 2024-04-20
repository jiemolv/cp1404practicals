from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi

def display_menu():
    print("q)uit, c)hoose taxi, d)rive")

def display_taxis(taxis):
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")

def main():
    current_taxi = None
    bill_to_date = 0.00
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]

    print("Let's drive!")
    display_menu()
    option = input(">>> ").lower()

    while option != 'q':
        if option == 'c':
            print("Taxis available:")
            display_taxis(taxis)
            try:
                taxi_choice = int(input("Choose taxi: "))
                if taxi_choice < 0 or taxi_choice >= len(taxis):
                    print("Invalid taxi choice")
                    print(f"Bill to date: ${bill_to_date:.2f}")
                else:
                    current_taxi = taxis[taxi_choice]
                    print(f"Bill to date: ${bill_to_date:.2f}")
            except ValueError:
                print("Invalid option")
                print(f"Bill to date: ${bill_to_date:.2f}")
        elif option == 'd':
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
            else:
                try:
                    distance = float(input("Drive how far? "))
                    current_taxi.start_fare()  # Reset fare distance
                    current_taxi.drive(distance)
                    cost = current_taxi.get_fare()
                    # cost = current_taxi.drive(distance)
                    bill_to_date += cost
                    print(f"Your {current_taxi.name} trip cost you ${cost:.2f}")
                    print(f"Bill to date: ${bill_to_date:.2f}")
                except ValueError:
                    print("Invalid distance")
                    print(f"Bill to date: ${bill_to_date:.2f}")
        else:
            print("Invalid option")
            print(f"Bill to date: ${bill_to_date:.2f}")

        display_menu()
        option = input(">>> ").lower()

    print(f"Total trip cost: ${bill_to_date:.2f}")
    print("Taxis are now:")
    display_taxis(taxis)

if __name__ == "__main__":
    main()