
def show_history()->None:
    print("\n Brief History of python:")
    print("\n Created in the year 1991:")
    print("\n py 3 in the year 2008:")

    print("\n*** Program that computes the average score of students:")

def get_names_score() -> tuple[list[str], list[float]]:
    while True:
        try:
            count = int(input("Number of students: "))
            if count <= 0:
                print("Please enter a number greater than 0")
                continue
                break
        except ValueError:
            print("invalid input")

        names_of_students = []
        scores = []

        print("\n Enter student names and scores:")

        for i in range(count):
            name = input(f'student {i+1} name: ').strip()
            if not name:
                name = f'Student {i+1}'
                names_of_students.append()

            while True:
                try:
                    score = float(input(f"Enter the score for {name}: "))
                    if 0 <= score <= 100:
                        scores.append(score)
                        break
                    else:
                        print("score must be between 0 and 100")

                except ValueError:
                    print("invalid input")

            return names_of_students, scores

