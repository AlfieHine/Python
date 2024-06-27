import random

# List of words to randomly choose from
word_list = [
    "apple", "banana", "cherry", "orange", "grape", "melon", "kiwi", "mango", "peach", "pear",
    "plum", "berry", "apricot", "avocado", "blueberry", "cantaloupe", "coconut", "cranberry", "fig", 
    "guava", "lemon", "lime", "mandarin", "nectarine", "papaya", "pineapple", "raspberry", 
    "strawberry", "watermelon", "carrot", "tomato", "cucumber", "spinach", "lettuce", "broccoli",
    "cauliflower", "onion", "garlic", "ginger", "pepper", "potato", "squash", "zucchini", "beetroot",
    "pumpkin", "eggplant", "corn", "yam"
]

# The ASCII art for each stage of the hangman
hangman_pics = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

# Function to display the welcome logo
def display_welcome():
    print('''
     _    _                                         
    | |  | |                                        
    | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
    |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
    | |  | | (_| | | | | (_| | | | | | | (_| | | | |
    |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                        __/ |                      
                       |___/           
          ''')

# Function to display the end message
def display_end_message(is_winner, word):
    if is_winner:
        print(''' 
 __     __          __          ___       _ 
 \ \   / /          \ \        / (_)     | |
  \ \_/ /__  _   _   \ \  /\  / / _ _ __ | |
   \   / _ \| | | |   \ \/  \/ / | | '_ \| |
    | | (_) | |_| |    \  /\  /  | | | | |_|
    |_|\___/ \__,_|     \/  \/   |_|_| |_(_)
              ''')
        print(f"Congratulations! You guessed the word {word}. You win!")
    else:
        print('''
   _____                         ____                 
  / ____|                       / __ \                
 | |  __  __ _ _ __ ___   ___  | |  | |_   _____ _ __ 
 | | |_ |/ _` | '_ ` _ \ / _ \ | |  | \ \ / / _ \ '__|
 | |__| | (_| | | | | | |  __/ | |__| |\ V /  __/ |   
  \_____|\__,_|_| |_| |_|\___|  \____/  \_/ \___|_|
               ''')
        print(f"You did not guess the word {word}. You lose :(")

# Function to get user input and ensure it is valid
def get_user_input(guessed_letters):
    while True:
        guess = input("Guess a letter: ").lower()
        if not guess.isalpha() or len(guess) != 1:
            print("Invalid input. Please enter a single alphabetic character.")
        elif guess in guessed_letters:
            print(f"You've already guessed {guess}")
        else:
            return guess

# Function to update the guessed positions in the word
def update_guessed_positions(word, guessed_positions, guess):
    for i, char in enumerate(word):
        if char == guess:
            guessed_positions[i] = char

# Function to display the current state of the game
def display_current_state(guessed_positions, hangman_pics, health):
    print(' '.join(guessed_positions))
    print(hangman_pics[health])

# Main function to play the hangman game
def hangman():
    display_welcome()
    
    while True:
        # Initialize game variables
        health = 0
        random_word = random.choice(word_list)
        guessed_positions = ["_"] * len(random_word)
        guessed_letters = set()

        while health < len(hangman_pics) - 1:
            display_current_state(guessed_positions, hangman_pics, health)
            
            # Check for win condition
            if "_" not in guessed_positions:
                display_end_message(True, random_word)
                break
            
            # Get a valid guess from the user
            letter_choice = get_user_input(guessed_letters)
            guessed_letters.add(letter_choice)

            # Check if the guess is in the word
            if letter_choice in random_word:
                update_guessed_positions(random_word, guessed_positions, letter_choice)
                print(f"You guessed {letter_choice}, that was in the word.")
            else:
                health += 1
                print(f"You guessed {letter_choice}, that's not in the word. You lose a life!")
        
        # Check for lose condition
        if "_" in guessed_positions:
            display_end_message(False, random_word)

        # Ask the user if they want to play again
        restart = input("Would you like to play again? (Y/N) ").upper()
        if restart != "Y":
            break

# Start the game
hangman()
