# Word Jumble
#
# The computer picks a random word and then "jumbles" it
# The player has to guess the original word

import random

# create a sequence of words to choose from
WORDS = ("python", "jumble", "easy", "difficult", "answer", "xylophone")
# pick one word randomly from the sequence
word = random.choice(WORDS)
# create a variable to use later to see if the guess is correct
correct = word

value=0

if word == "python":
    hint="Programing language"
elif word == "jumble":
    hint=("Another word for mixing up")
elif word == "easy":
    hint=("Another word for simple")
elif word == "difficult":
    hint=("The opposite of simple")
elif word == "answer":
    hint=("solution")
elif word == "xylophone":
    hint=("Musical instrument")

# create a jumbled version of the word
jumble =""
while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position + 1):]

# start the game
print(
"""
           Welcome to Word Jumble!
        
   Unscramble the letters to make a word.
(Press the enter key at the prompt to quit.)
"""
)
print("The jumble is:", jumble)

guess = input("\nYour guess: ")
while guess != correct and guess != "":
    if guess == "hint":
        print(hint)
        value=value+1
    elif guess != word:
        print("Sorry, that's not it.")
    guess = input("Your guess: ")
    
if guess == correct:
    print("That's it!  You guessed it!\n")
    if value == 0:
        print("YAY!! You are smart enough to solve the word without help!")

print("Thanks for playing.")

input("\n\nPress the enter key to exit.")
