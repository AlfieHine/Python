import random 

#List of words to randomly choose from
word_list = [
    "apple", "banana", "cherry", "orange", "grape", "melon", "kiwi", "mango", "peach", "pear",
    "plum", "berry", "apricot", "avocado", "blueberry", "cantaloupe", "coconut", "cranberry", "fig", 
    "guava", "lemon", "lime", "mandarin", "nectarine", "papaya", "pineapple", "raspberry", 
    "strawberry", "watermelon", "carrot", "tomato", "cucumber", "spinach", "lettuce", "broccoli",
    "cauliflower", "onion", "garlic", "ginger", "pepper", "potato", "squash", "zucchini", "beetroot",
    "pumpkin", "eggplant", "corn", "yam", "cherry", "plum"
]

#The ascii art for each stage of the hangman
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

#The function thats called for starting/restarting the game
def Game():
    #Welcome logo
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
    
    #Resetting varibles for the start of reach round
    health = 0
    random_word = random.choice(word_list)
    guessed_positions = ["_"] * len(random_word)


    #Loop to consistently ask for a guess until the player runs out of lives or the word is guessed
    while True:
      
      #If statement to determine the win or lose conditions
      if health == 6:
        print('''
   _____                         ____                 
  / ____|                       / __ \                
 | |  __  __ _ _ __ ___   ___  | |  | |_   _____ _ __ 
 | | |_ |/ _` | '_ ` _ \ / _ \ | |  | \ \ / / _ \ '__|
 | |__| | (_| | | | | | |  __/ | |__| |\ V /  __/ |   
  \_____|\__,_|_| |_| |_|\___|  \____/  \_/ \___|_|
               ''')
        print(f"You did not guess the word {random_word}. You lose :(")
        restart = input("Would you like to play again? (Y/N) ")
        if restart.upper() == "Y":
          Game()
        else:
          exit()
      elif "_" not in guessed_positions:
        print(''' 
 __     __          __          ___       _ 
 \ \   / /          \ \        / (_)     | |
  \ \_/ /__  _   _   \ \  /\  / / _ _ __ | |
   \   / _ \| | | |   \ \/  \/ / | | '_ \| |
    | | (_) | |_| |    \  /\  /  | | | | |_|
    |_|\___/ \__,_|     \/  \/   |_|_| |_(_)
              ''')
        print(f"Congratulations! You guessed the word {random_word}. You win!")
        restart = input("Would you like to play again? (Y/N) ")
        if restart.upper() == "Y":
          Game()
        else:
          exit()
      
      #Recieve a guess
      letter_choice = input("Guess a letter: ")

      #Convert to lower case then check to see if the guess is within the random word choosen
      if letter_choice.lower() in random_word.lower():
        for i, char in enumerate(random_word.lower()):
          #If it is, the letter is added to the correct possition in the array e.g. Guess = "l". Program shows _ _ _ l _ for the word apple
          if char == letter_choice.lower():
            guessed_positions[i] = random_word[i]

        print(' '.join(guessed_positions))
        print(f"You guessed {letter_choice}, that was in the word.")
        print(hangman_pics[health])

      #Remove health if the guess is wrong
      else:
        health += 1
        print(' '.join(guessed_positions))
        print(f"You guessed {letter_choice}, thats not in the word. You lose a life!")
        print(hangman_pics[health])

#Starting the game     
Game()