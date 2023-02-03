'''
The hangman game is a word guessing game where the player is given a word and has to
 guess the letters that make up the word. 
The player is given a certain number of tries (no more than 6 wrong guesses are allowed)
 to guess the correct letters before the game
 is over.
'''

'''
EXAMPLE

You have 6 tries left.                                                                                                                                           
Used letters:                                                                                                                                                    
Word: _ _ _ _                                                                                                                                                    
Guess a letter: a 

You have 6 tries left.                                                                                                                                           
Used letters: a                                                                                                                                                  
Word: _ a _ a                                                                                                                                                    
Guess a letter: j    

You have 6 tries left.                                                                                                                                           
Used letters: j a                                                                                                                                                
Word: j a _ a                                                                                                                                                    
Guess a letter: v                                                                                                                                                
You guessed the word java !
'''
import random

def hagman():
    words = ['python','apple', 'java', 'oracle','atlas']
    word = random.choice(words)
    guesses = ['_']*len(word)
    guess_str = "".join(guesses)
    useLetters = ""
    tries = 6
    while tries:
        print(f"You have {tries}")
        print(f"Used letters: {useLetters}")
        print(f"Word: {guess_str}")
        guess = input("Guess a letter: ")
        useLetters += guess

        if guess in useLetters[:-1]:
            print(f"You have already used {guess}")
        elif guess in word:
            for i in range(len(word)):
                if guess == word[i]:
                    guesses[i] = guess
            guess_str = "".join(guesses)
            if guess_str == word:
                print(f'You guessed the word {word} !')
                break
        else:
            tries -= 1
            if tries == 0:
                print('Sorry...You failed to guess the word!')
hagman()









