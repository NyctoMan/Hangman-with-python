import random
import pygame
from Wordlist import word_list
from stages import stages, logo

# Initialize pygame mixer for sound effects
pygame.mixer.init()

# Load sound effects
wrong_sound = pygame.mixer.Sound("wrong_sound.mp3")
clap_sound = pygame.mixer.Sound("clap_sound.mp3")

def play_again():
    """Ask the player if they want to play again."""
    while True:
        choice = input("Would you like to play again? (yes/no): ").lower()
        if choice == "yes":
            return True
        elif choice == "no":
            return False
        else:
            print("Invalid choice. Please enter 'yes' or 'no'.")

def welcome_message():
    """Display a welcome message to the player."""
    print("Welcome to the Hangman Game!")

# Display welcome message
welcome_message()

while True:
    # Initialize game variables
    end_of_game = False
    chosen_word = random.choice(word_list)
    word_length = len(chosen_word)
    lives = 6

    # Display game logo
    print(logo)

    # Create blanks for the word to be guessed
    display = ["_" for _ in range(word_length)]

    # Main game loop
    while not end_of_game:
        # Get user input for guessing a letter
        guess = input("Guess a letter: ").lower()

        # Check if the guessed letter has already been guessed
        if guess in display:
            print(f"You've already guessed {guess}")

        # Check if the guessed letter is in the chosen word
        for position in range(word_length):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter

        # Check if the guessed letter is incorrect
        if guess not in chosen_word:
            lives -= 1
            print(f"You guessed {guess}, That's not in the word. You lose a life!")
            wrong_sound.play()
            if lives == 0:
                end_of_game = True
                print("You lose.")
                print(f"The chosen word was : {chosen_word}")

        # Check if the guessed letter is correct
        if guess in chosen_word and guess not in display:
            clap_sound.play()

        # Display the current state of the word
        print(" ".join(display))

        # Check if the player has guessed all letters
        if "_" not in display:
            end_of_game = True
            print("You win. :D")

        # Print the ASCII art representing the current state of the hangman
        print(stages[lives])

    # Ask the player if they want to play again
    if not play_again():
        print("Thanks for playing!")
        break
