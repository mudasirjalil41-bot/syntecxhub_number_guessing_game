import  random

def play_game():
    print("\n==================================")
    print("    NUMBER GUESSING GAME          ")
    print("==================================")
    print("Select Difficulty Level:")
    print("1. Easy (1 to 50)")
    print("2. Medium (1 to 100)")
    print("3. Hard (1 to 200)")

    choice = input("Option (1-3) ")
    if choice == '1':
        max_range = 50

    elif choice == '2':
        max_range = 100

    else:
        max_range = 200

    secret_number = random.randint(1,max_range)
    attempts = 0

    print(f"\nI have thought of a number between 1 and {max_range}. Take a guess!")

    while True:
        try:
            guess = int(input("enter a guess: "))
            attempts += 1


            if guess > secret_number :
                print('Try a lower number.')

            elif guess < secret_number  :
               print('Try a higher number.')

            else:
               print(f"\n🎉 Congratulations! You guessed the correct number in {attempts} attempts!")
               return attempts

        except ValueError:
            print("Invalid input! Please enter a valid integer.")

def main_game():
    best_score = None
    while True:
      attempts = play_game()

      if best_score is None or attempts < best_score:
          best_score = attempts
          print(f"⭐ New Best Score: Only {best_score} attempts!")

      else:
          print(f"🏆 Your Best Score so far: {best_score} attempts.")

      replay = input("\nDo you want to play again? (yes/no): ").strip().lower()
      if replay not in ['y', 'yes']:
          print("\nThanks for playing! Goodbye.")
          break

if __name__ == "__main__":
    main_game()





