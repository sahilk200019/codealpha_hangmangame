import random #for using random values in our programm



# List of words to choose from
words = []
bird_words=['sparrow','crow','flamingo','eagle','kite','parrot','owl','humminburd']
animal_words=['Lion','tiger','cheetah','cow','dog','platipus','zebra','chimpange']
programming_words=['keywords','async','algorithm','binary','compiler','error']
bollywood_words=['Salman ', 'sahruk','aamir','ajay','priyanka','imran','shaktikapoor']
holliwood_words=actor_names = ['Leonardo', 'Brad', 'Johnny', 'Tom', 'Robert', 'Chris', 'Will']

#finding the interest area of player 
print(""" Please select in which feild you want to play
      Press 1 : Bird knowledge
      Press 2 : Animal Knwledge
      Press 3 : Programming words
      Press 4 : Bollywood 
      Press 5 : Holliwood """)


valueo_of_interest=int(input())
match valueo_of_interest:
    case 1:
        words=bird_words
    case 2:
        words=animal_words
    case 3:
        words=programming_words
    case 4: 
        words=bollywood_words
    case 5:
        words=holliwood_words
    
# Hangman states represented by graphic dashes
hangman_stages = [
    """
    -----
    |   |
        |
        |
        |
        |
    --------
    """,
    """
    -----
    |   |
    O   |
        |               
        |
        |
    --------
    """,
    """
    -----
    |   |
    O   |
    |   |
        |
        |
    --------
    """,
    """
    -----
    |   |
    O   |
   /|   |
        |
        |
    --------
    """,
    """
    -----
    |   |
    O   |
   /|\\  |
        |
        |
    --------
    """,
    """
    -----
    |   |
    O   |
   /|\\  |
   /    |
        |
    --------
    """,
    """
    -----
    |   |
    O   |
   /|\\  |
   / \\  |
        |
    --------
    """
]

# Function to take  a random word
def word_choosen():
    return random.choice(words)

# Function to display the current state of the word
def show_word(word, guessed_letters):
    return ''.join([letter if letter in guessed_letters else '_' for letter in word])

# Function to play the hangman game
def play_hangman():
    word = word_choosen()
    guessed_letters = set()
    incorrect_guesses = 0
    max_incorrect_guesses = len(hangman_stages) - 1

    print("Welcome to Hangman!")
    print(f"The word has {len(word)} letters.")
    
    while incorrect_guesses < max_incorrect_guesses:
        print(hangman_stages[incorrect_guesses])
        print("Current word:", show_word(word, guessed_letters))
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter.")
        elif guess in word:
            print("Good guess!")
            guessed_letters.add(guess)
        else:
            print("Incorrect guess.")
            incorrect_guesses += 1
            print(f"You have {max_incorrect_guesses - incorrect_guesses} guesses left.")
        
        if set(word).issubset(guessed_letters):
            print(f"Congratulations! You guessed the word: {word}")
            break
    else:
        print(hangman_stages[incorrect_guesses])
        print(f"Game over! The word was: {word}")

# Run the game
if __name__ == "__main__":
    play_hangman()
