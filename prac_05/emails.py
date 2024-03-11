
def extract_name(email):
    name = email.split('@')[0]
    return ' '.join(name.split('.')).title()

def main():
    users = {}
    while True:
        email = input("Email: ")
        if not email:
            break

        name = extract_name(email)
        confirm_name = input(f"Is your name {name}? (Y/n) ").lower()

        if confirm_name == 'n':
            name = input("Name: ").title()
        elif confirm_name != 'y' and confirm_name != '':
            name = input("Name: ").title()

        users[email] = name

    print("\nStored users' details:")
    for email, name in users.items():
        print(f"{name} ({email})")

if __name__ == "__main__":
    main()