import random

# List of words to choose from
words = ['apple', 'banana', 'orange', 'pear', 'grape']

# Choose a random word from the list
word = random.choice(words)

# Initialize the guesses
guesses = ''

# Set the number of turns
turns = 6
#pyinstaller --name=YourAppName --onefile C:\Users\kolya\PycharmProjects\pythonProject\venv\111.py

# Loop until the player has run out of turns or has guessed the word
while turns > 0:
    # Counter for failed attempts
    failed = 0

    # Display the word with underscores for unguessed letters
    for char in word:
        if char in guesses:
            print(char, end=' ')
        else:
            print('_', end=' ')

            # Increment the failed counter
            failed += 1

    # If all letters have been guessed, the player wins
    if failed == 0:
        print('\nCongratulations! You win!')
        break

    # Get the player's guess
    guess = input('\nGuess a letter: ')

    # Add the guess to the list of guesses
    guesses += guess

    # If the guess is not in the word, decrement the number of turns
    if guess not in word:
        turns -= 1
        print('\nWrong guess. You have', turns, 'turns left.')

        # If the player has run out of turns, display the word and end the game
        if turns == 0:
            print('\nSorry, you lose. The word was', word)
