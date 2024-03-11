
# TODO: Reformat this file so the dictionary code follows PEP 8 convention
CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}

for state_code, state_name in CODE_TO_NAME.items():
    print(f"{state_code.upper()} is {state_name}")

while True:
    state_code = input("Enter short state: ").upper()   # Convert input to uppercase

    if state_code == "":
        break
    try:
        state_name = CODE_TO_NAME[state_code]
        print(f"{state_code.upper()} is {state_name}")
    except KeyError:
        print("Invalid short state")
