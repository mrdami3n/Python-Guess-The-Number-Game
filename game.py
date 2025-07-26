import random
import time

def guess_the_number():
    """
    A simple 'Guess the Number' game.
    The computer picks a number between 1 and 100, and the player tries to guess it.
    """
    
    # --- Game Setup ---
    player_name = input("Hello! What's your name? ")
    print(f"Welcome, {player_name}! I'm thinking of a number between 1 and 100.")
    
    # Generate the secret number
    secret_number = random.randint(1, 100)
    
    # --- Game Variables ---
    guesses_taken = 0
    max_guesses = 10 # You can change this to make the game easier or harder
    
    print(f"You have {max_guesses} chances to guess it. Good luck!\n")
    
    # --- Main Game Loop ---
    while guesses_taken < max_guesses:
        try:
            # Prompt the player for their guess
            guess_str = input("Take a guess: ")
            
            # Check if the input is a valid number
            if not guess_str.isdigit():
                print("Oops! That doesn't look like a number. Please enter a whole number.")
                continue

            guess = int(guess_str)
            guesses_taken += 1

            # --- Compare Guess to Secret Number ---
            if guess < secret_number:
                remaining_guesses = max_guesses - guesses_taken
                print(f"Your guess is too low. You have {remaining_guesses} guesses left.")
            
            elif guess > secret_number:
                remaining_guesses = max_guesses - guesses_taken
                print(f"Your guess is too high. You have {remaining_guesses} guesses left.")
            
            else:
                # This condition is met if the guess is correct
                break # Exit the loop because the player won

        except ValueError:
            # This handles cases where the input is not a number, though the isdigit() check is more user-friendly.
            print("Invalid input. Please enter a number.")

    # --- Game Over ---
    # This part of the code runs after the loop finishes (either by winning or running out of guesses)
    
    time.sleep(1) # Add a small pause for dramatic effect

    if guess == secret_number:
        print(f"\nCongratulations, {player_name}! You guessed the number in {guesses_taken} tries!")
    else:
        print(f"\nSorry, {player_name}. You've run out of guesses.")
        print(f"The number I was thinking of was {secret_number}.")

# --- Run the game ---
if __name__ == "__main__":
    guess_the_number()
