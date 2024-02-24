# # TODO: Fix this!
# score = float(input("Enter score: "))
# if score < 0:
#     print("Invalid score")
# else:
#     if score > 100:
#         print("Invalid score")
#     if score > 50:
#         print("Passable")
#     if score > 90:
#     print("Excellent")
# if score < 50:
#     print("Bad")


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

def main():
    user_score = float(input("Enter score: "))
    result = determine_result(user_score)
    print(f"Your result:{result}")

    # Generate random score
    random_score = random.randint(0,101)
    print(f"Random score:{random_score}")
    random_result = determine_result(random_score)
    print(f"Random result:{random_result}")

main()