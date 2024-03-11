
import csv


def read_wimbledon_data(filename):
    champions_count = {}
    countries_set = set()

    with open(filename, "r", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)
        for row in reader:
            champion = row['Champion']
            country = row['Country']

            champions_count[champion] = champions_count.get(champion, 0) + 1
            countries_set.add(country)

    return champions_count, countries_set


def display_champions(champions_count):
    print("Wimbledon Champions:")
    for champion, count in sorted(champions_count.items()):
        print(f"{champion} {count}")


def display_countries(countries_set):
    countries_list = sorted(countries_set)
    countries_str = ", ".join(countries_list)
    print(f"\nThese {len(countries_list)} countries have won Wimbledon:")
    print(countries_str)


def main():
    filename = 'wimbledon.csv'
    champions_count, countries_set = read_wimbledon_data(filename)
    display_champions(champions_count)
    display_countries(countries_set)


if __name__ == "__main__":
    main()
