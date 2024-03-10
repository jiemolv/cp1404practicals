
FILENAME = "subjcet_data.txt"


def main():
    data = get_data()
    display_subject_details(data)

def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    subjects = []
    with open(FILENAME) as input_file:
        for line in input_file:
            line = line.strip()  # Remove the \n
            parts = line.split(',')  # Separate the data into its parts
            parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
            subjects.append(parts)
        # print(subjects)
        return subjects  # WHY can't return the subjects value? I don't know where went wrong


def display_subject_details(data):
    for subject in data:
        print(f"{subject[0]} is taught by {subject[1]} and has {subject[2]} students.")

main()


