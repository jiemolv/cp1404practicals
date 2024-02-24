import random

def determine_result(score):
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    elif score > 0:
        return "Bad"
    else:
        return "Invalid score"

def get_vaild_score():
    while True:
        score = float(input("Enter a valid score (0-100)"))
        if 0 <= score <= 100:
            return score
        else:
            print(f"Invalid score. Please enter a score between 0 and 100.")

def print_result(score):
    result = determine_result(score)
    print(f"Result:{result}")

def show_stars(score):
    print("*" * int(score))

def main():
    user_score = get_vaild_score()

    while True:
        print("\nMenu:")
        print("(G)et a valid score")
        print("(P)rint result")
        print("(S)how stars")
        print("(Q)uit")

        choice = input(">>> ").upper()

        if choice == "G":
            user_score = get_vaild_score()
        elif choice == "P":
            print_result(user_score)
        elif choice == "S":
            show_stars(user_score)
        elif choice == "Q":
            print("Thank you. Goodbye!")
            break
        else:
            print("Invalid input. Please select a valid option.")

main()

# def display_menu():
#     print("\nMenu:")
#     print("(G)et a valid score")
#     print("(P)rint result")
#     print("(S)how stars")
#     print("(Q)uit")
#
# def main():
#     user_score = get_vaild_score()
#     user_menu = dispaly_menu()
#     choice = input(">>>").upper()
#
# while choice != "Q":
#     if choice == "G":
#         user_score = get_vaild_score()
#     elif choice == "P":
#         print_result(user_score)
#     elif choice == "S":
#         show_stars(user_score)
#     else:
#         print("Invalid choice")
#
#     choice = input(">>>").upper()
# print("Finished")



