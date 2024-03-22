
from prac_06.guitar import Guitar

def main():
    guitars = []
    print("My guitars")
    i = 1
    while True:
        name = input(f"Name of guitar {i} (Enter blank to exit):")
        if name == " ":
            break
        year = int(input(f"Year of Guitar {i}:"))
        cost = float(input(f"Cost of Guitar {i} ($):"))
        print(f"{name} {year} : ${cost:.2f} added")
        guitars.append(Guitar(name, year, cost))
        i += 1

    print("\nThese are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        vintage_string = "(vintage)" if guitar.is_vintage(2023) else ""
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}) worth ${guitar.cost:10,.2f} {vintage_string}")

if __name__ == '__main__':
    main()