import random

leaderboard = []

# 1. Print Instructions
def print_instructions():
    print("\n🎯 Welcome to the 'Guess the Number' Game!")
    print("Your goal is to guess the randomly generated number.")
    print("You will receive hints after each incorrect guess.")
    print("Try to guess the number in as few attempts as possible!\n")

# 2. Settings Menu
def settings_menu():
    while True:
        print("\n⚙️ SETTINGS MENU")
        print("1. Select Difficulty Level")
        print("2. Set Custom Range")
        print("3. View Leaderboard")
        print("4. Exit Settings")

        choice = input("Choose an option (1-4): ")

        if choice == '1':
            return get_difficulty_level()
        elif choice == '2':
            return set_custom_range()
        elif choice == '3':
            view_leaderboard()
        elif choice == '4':
            return None
        else:
            print("❌ Invalid choice. Please select 1-4.")

# 3. Difficulty Levels
def get_difficulty_level():
    print("\n📊 Difficulty Levels")
    print("1. Easy (1-10, 5 attempts)")
    print("2. Medium (1-50, 7 attempts)")
    print("3. Hard (1-100, 10 attempts)")

    choice = input("Select difficulty (1-3): ")
    if choice == '1':
        return (1, 10, 5)
    elif choice == '2':
        return (1, 50, 7)
    elif choice == '3':
        return (1, 100, 10)
    else:
        print("❌ Invalid choice. Defaulting to Medium.")
        return (1, 50, 7)

# 4. Custom Range
def set_custom_range():
    try:
        start = int(input("Enter start of range: "))
        end = int(input("Enter end of range: "))
        attempts = int(input("Enter max number of attempts: "))
        if start >= end or attempts <= 0:
            print("❌ Invalid range or attempts. Try again.")
            return set_custom_range()
        return (start, end, attempts)
    except ValueError:
        print("❌ Please enter valid integers.")
        return set_custom_range()

# 5. Leaderboard
def view_leaderboard():
    print("\n🏆 Leaderboard")
    if not leaderboard:
        print("No scores yet.")
    else:
        for idx, entry in enumerate(sorted(leaderboard, key=lambda x: x['score'], reverse=True), start=1):
            print(f"{idx}. {entry['name']} - Score: {entry['score']}")

# 6. Advanced Hint System
def provide_hint(number_to_guess, guess):
    hints = []
    if number_to_guess % 2 == 0:
        hints.append("Hint: The number is EVEN.")
    else:
        hints.append("Hint: The number is ODD.")

    if guess != 0 and number_to_guess % guess == 0:
        hints.append(f"Hint: The number IS divisible by {guess}.")
    else:
        hints.append(f"Hint: The number is NOT divisible by {guess}.")

    if is_prime(number_to_guess):
        hints.append("Hint: The number is PRIME.")
    else:
        hints.append("Hint: The number is NOT PRIME.")

    return hints

# 7. Prime Checking
def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num**0.5)+1, 2):
        if num % i == 0:
            return False
    return True

# 8. Play Single Round
def play_round(start, end, max_attempts):
    number_to_guess = random.randint(start, end)
    attempts = 0
    print(f"\n🎮 Guess a number between {start} and {end}. You have {max_attempts} attempts.")

    while attempts < max_attempts:
        try:
            guess = int(input(f"Attempt {attempts+1}: Your guess? "))
            attempts += 1

            if guess == number_to_guess:
                print(f"✅ Correct! You guessed the number in {attempts} attempts.")
                return max(0, (max_attempts - attempts + 1) * 10)
            else:
                print("❌ Incorrect guess.")
                for hint in provide_hint(number_to_guess, guess):
                    print(hint)
        except ValueError:
            print("❌ Enter a valid number.")

    print(f"😢 You've used all your attempts. The number was {number_to_guess}.")
    return 0

# 9. Main Game
def guess_the_number():
    print_instructions()

    while True:
        settings = settings_menu()
        if settings is None:
            print("Exiting settings...")

        start, end, max_attempts = settings or (1, 50, 7)
        player_name = input("\nEnter your name: ")
        score = play_round(start, end, max_attempts)

        leaderboard.append({'name': player_name, 'score': score})
        print(f"🎉 {player_name}, your score: {score}")

        again = input("Play another round? (y/n): ").lower()
        if again != 'y':
            print("\n👋 Thanks for playing! Final Leaderboard:")
            view_leaderboard()
            break

# Run the game
if __name__ == "__main__":
    guess_the_number()