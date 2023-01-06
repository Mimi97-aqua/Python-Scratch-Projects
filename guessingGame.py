#guessing game
#Task: 1. Build a number-guessing game. when I come in as user I would run the code from my IDE. When I Run the code
#1. it will ask for my name.
#When I enter my name
#2. It will ask me to guess a number.
#When I type in a number it will tell me if I’m hot or if I’m cold.
#Hot => means I'm getting close to the right number.
#Cold => means I’m far from guessing the right number.

#When I guess the right number it will tell I won after X tries. X being the number of guesses I made.
#Then it will ask if I want to play again or leave the game.

#N.B: every time I play the game I get a random number to guess

import random
import math
def guessing_game_function():
    name = input("Enter your name: ")
    print("Welcome ", name)
    lowerBound = 0
    upperBound = 50
    #generating random number,x,between set lowerbound and upperbound
    x = random.randint(lowerBound, upperBound)
    print("INSTRUCTION: You are to guess a number from 0 to 50")
    print("NOTE: You've only ",
           round(math.log(upperBound - lowerBound + 1, 2)),
          " chances to guess the right number!\n")
    #initializing number of guesses
    count = 0
    while count < math.log(upperBound - lowerBound + 1, 2):
        count += 1
        guess = int(input("Guess a number:- "))
        if x == guess:
            print("Congratulations you guessed after ",
                  count, " tries")
            break
        elif x > guess:
            print("Hot")
        elif x < guess:
            print("cold")
    #if user exhausts maximum number of guesses
    if count >= math.log(upperBound - lowerBound + 1, 2):
        print("\nThe number is %d" % x , "Try again")

guessing_game_function()

answer = input("Do you wish to play again? YES or NO: ")
if answer == "YES" or answer == "Yes" or answer == "yes":
    guessing_game_function()
elif answer == "NO" or answer == "No" or answer == "no":
    print("Close IDE")
