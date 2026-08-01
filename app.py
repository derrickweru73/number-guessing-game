import random

# ----------------------------
# Choose Difficulty
# ----------------------------
def choose_difficulty():
    print("\n========== Difficulty Levels ==========")
    print("1. Easy   (10 Attempts)")
    print("2. Medium (7 Attempts)")
    print("3. Hard   (5 Attempts)")

    while True:
        choice = input("Choose difficulty (1-3): ")

        if choice == "1":
            return 10
        elif choice == "2":
            return 7
        elif choice == "3":
            return 5
        else:
            print("Invalid choice. Please select 1, 2 or 3.")


# ----------------------------
# Save Score
# ----------------------------
def save_score(username, attempts):
    with open("highscores.txt", "a") as file:
        file.write(f"{username},{attempts}\n")


# ----------------------------
# Leaderboard
# ----------------------------
def show_leaderboard():
    print("\n========== LEADERBOARD ==========")

    try:
        with open("highscores.txt", "r") as file:
            scores = []

            for line in file:
                name, score = line.strip().split(",")
                scores.append((name, int(score)))

            if len(scores) == 0:
                print("No scores available.")
                return

            scores.sort(key=lambda x: x[1])

            print("{:<15} {}".format("Player", "Attempts"))
            print("-" * 30)

            for name, score in scores:
                print("{:<15} {}".format(name, score))

    except FileNotFoundError:
        print("No leaderboard yet.")


# ----------------------------
# Hint Function
# ----------------------------
def give_hint(number):
    print("\n********** HINT **********")

    if number % 2 == 0:
        print("The number is EVEN.")
    else:
        print("The number is ODD.")

    if number % 5 == 0:
        print("The number is divisible by 5.")
    else:
        print("The number is NOT divisible by 5.")

    if number > 50:
        print("The number is greater than 50.")
    else:
        print("The number is 50 or less.")

    print("**************************")


# ----------------------------
# Play Game
# ----------------------------
def play_game():

    print("\n===================================")
    print("      NUMBER GUESSING GAME")
    print("===================================")

    username = input("Enter your username: ")

    total_attempts = choose_difficulty()

    secret_number = random.randint(1, 100)

    attempts_used = 0
    wrong_guesses = 0

    while attempts_used < total_attempts:

        remaining = total_attempts - attempts_used

        print(f"\nRemaining Attempts: {remaining}")

        try:
            guess = int(input("Guess a number (1-100): "))

        except ValueError:
            print("Please enter numbers only.")
            continue

        if guess < 1 or guess > 100:
            print("Number must be between 1 and 100.")
            continue

        attempts_used += 1

        if guess == secret_number:

            print("\nCongratulations!")
            print("You guessed the correct number.")

            print(f"You used {attempts_used} attempt(s).")

            save_score(username, attempts_used)

            return

        elif guess > secret_number:
            print("Too High!")
            wrong_guesses += 1

        else:
            print("Too Low!")
            wrong_guesses += 1

        if wrong_guesses == 3:
            give_hint(secret_number)

    print("\nGame Over!")
    print(f"The correct number was {secret_number}.")


# ----------------------------
# Main Menu
# ----------------------------
while True:

    print("\n==============================")
    print("1. Play Game")
    print("2. View Leaderboard")
    print("3. Exit")
    print("==============================")

    choice = input("Choose an option: ")

    if choice == "1":
        play_game()

    elif choice == "2":
        show_leaderboard()

    elif choice == "3":
        print("Thank you for playing!")
        break

    else:
        print("Invalid option.")