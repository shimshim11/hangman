import random

#Create a list of fruits
word_list = ["apple", "pear", "grapes", "watermelon", "orange"]
print(word_list)

#Choose a random fruit from the list
word = random.choice(word_list)
print(word)

#Function which iteratively checks if the input is valid guess
def ask_for_input():
    while True:
        guess = input("Enter a single letter: ")
        if len(guess) and guess.isalpha():
            print("Good guess!")
            guessed = check_guess(guess)
            if guessed:
                break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")

#Checks whether guess is in the word
def check_guess():
    #Convert the guess into lower case
    guess = guess.lower()

    if guess in word:
        print(f"Good guess! {guess} is in the word.")
        return True
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")
        return False