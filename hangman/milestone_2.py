import random
import string

#Create a list of fruits
word_list = ["apple", "pear", "grapes", "watermelon", "orange"]
print(word_list)

#Choose a random fruit from the list
word = random.choice(word_list)
print(word)

#Ask the user for an input of a fruit of their choice
guess = input("Enter a single letter: ")

#User validation; checking if the input is a single character
if len(guess) == 1 and guess in string.ascii_letters:
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")