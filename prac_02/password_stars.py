def get_valid_password(min_password_length):
    while True:
        password = str(input("Enter a password: "))
        if len(password) < min_password_length:
            print(f"Invalid input")
        else:
            return password
def print_asterisks(password):
    print("*" * len(password))

def main():
    min_password_length = 8
    password = get_valid_password(min_password_length)
    print_asterisks(password)

main()


