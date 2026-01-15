"""
Example 3: Number Guessing Game
Demonstrates loops, conditionals, and user input.
"""

import random

def play_game():
    """Play a number guessing game."""
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    # Generate random number
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 10
    
    while attempts < max_attempts:
        try:
            guess = int(input(f"\nAttempt {attempts + 1}/{max_attempts} - Enter your guess: "))
            attempts += 1
            
            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100!")
                continue
            
            if guess < secret_number:
                print("Too low! Try a higher number.")
            elif guess > secret_number:
                print("Too high! Try a lower number.")
            else:
                print(f"\nCongratulations! You guessed it in {attempts} attempts!")
                print(f"The number was {secret_number}")
                return
        
        except ValueError:
            print("Invalid input! Please enter a number.")
            attempts += 1
    
    print(f"\nGame Over! You've used all {max_attempts} attempts.")
    print(f"The number was {secret_number}")

def main():
    """Main function to run the game."""
    play_again = True
    
    while play_again:
        play_game()
        
        response = input("\nDo you want to play again? (yes/no): ").lower()
        play_again = response == "yes" or response == "y"
    
    print("\nThanks for playing!")

if __name__ == "__main__":
    main()
