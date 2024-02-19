# name = str(input('Enter name: '))
# choice =
# while choice != Q:
#     if choice == H:
#        print(f'{name}')
#     elif choice == G:
#        print(f'{name}')
#     else:
#         print(f'Invalid choice')
#    display menu
#     name = str(input('Enter name: '))
# print(f'Finished')

name = input("Enter name: ")
def display_menu():
    print("(H)ello")
    print("(G)oodbye")
    print("(Q)uit")

display_menu()
choice = input(">>> ").upper()

while choice != 'Q':
    if choice == 'H':
        print("Hello", name)
    elif choice == 'G':
        print("Goodbye", name)
    else:
        print("Invalid choice")

    display_menu()
    choice = input(">>> ").upper()

print("Finished.")