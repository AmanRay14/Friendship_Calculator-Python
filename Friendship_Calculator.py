def friendship_percentage_calculator():
    print("Welcome to the Friendship Percentage Calculator!")
    person1 = input("Enter the name of the first person: ")
    person2 = input("Enter the name of the second person: ")

    # You can define your own criteria/questions and weights here
    criteria = [
        {"question": "How often do you hang out together? (0-10): ", "weight": 0.2},
        {"question": "Do you have similar interests? (yes/no): ", "weight": 0.3},
        {"question": "How well do you communicate? (0-10): ", "weight": 0.2},
        {"question": "Do you trust each other? (yes/no): ", "weight": 0.3},
    ]

    total_score = 0
    max_score = 0

    for criterion in criteria:
        answer = input(f"{person1}, {criterion['question']}").lower()
        if answer == "yes":
            score = 10
        elif answer == "no":
            score = 0
        else:
            try:
                score = float(answer)
            except ValueError:
                print("Invalid input. Assuming a neutral score of 5.")
                score = 5

        total_score += score * criterion["weight"]
        max_score += 10 * criterion["weight"]

    friendship_percentage = (total_score / max_score) * 100

    print(f"\nFriendship Percentage between {person1} and {person2}: {friendship_percentage:.2f}%")

if __name__ == "__main__":
    friendship_percentage_calculator()
