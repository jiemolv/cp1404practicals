import random

MAX_NUMBER = 45
MIN_NUMBER = 1
PICK_TIMES = 6

def generate_unique_numbers():
    numbers = []
    while len(numbers) < PICK_TIMES:
        new_number = random.randint(MIN_NUMBER, MAX_NUMBER)
        if new_number not in numbers:
            numbers.append(new_number)
    return sorted(numbers)

def display_quick_picks(num_picks):
    for i in range(num_picks):
        quick_pick = generate_unique_numbers()
        print(" ".join(f"{number:2}" for number in quick_pick))

def main():
    num_quick_picks = int(input("How many quick picks? "))
    display_quick_picks(num_quick_picks)

if __name__ == '__main__':
    main()



