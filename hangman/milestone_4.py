import random

class Hangman():
    #Hangman class created with the initalised attributes of the game
    def __init__(self, word_list, num_lives=5) -> None:
        self.word_list = word_list
        self.num_lives = num_lives
        
        self.word = random.choice(self.word_list)
        self.word_guessed = ["_"] * len(self.word)
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []

    #Methods created for running checks of the guesses
    def check_guess(self, guess):
        guess = guess.lower()

        if guess in self.word:
            print(f"Good guess! {guess} is in the word!")

            for index, letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[index] = letter
                    break
            self.num_letters -= 1
            print(self.word_guessed)
        
        else:
            print(f"Sorry, {guess} is not in the word.")
            self.num_lives -= 1
            print(f"You have {self.num_lives} lives left.")

    #Ask the user for an input of a guess
    def ask_for_input(self):
        while True:
            guess = input("Enter a single letter: ")

            if len(guess) != 1 and not guess.isalpha():
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.list_of_guesses.append(guess)
                self.check_guess(guess)

hangman = Hangman(["apple", "pear", "grapes", "watermelon", "orange"])
hangman.ask_for_input()