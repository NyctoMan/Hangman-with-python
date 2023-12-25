import random
from Wordlist import word_list
from stages import stages , logo

end_of_game = False
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
lives = 6
print(logo)

#Create blanks
display = []
for _ in range(word_length):
    display += "_"
# Main game
while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You've already guessed {guess}")
    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
            
    #Check if user is wrong.
    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, That's not in the word. You lose a life!")
        if lives == 0:
            end_of_game = True
            print("You lose.")
            print(f"The chosen word was : {chosen_word}")

    # Join all elements to a str
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win. :D")

    # Print the ASCII art from 'stages'
    print(stages[lives])
