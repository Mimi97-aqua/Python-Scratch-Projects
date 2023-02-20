import random 
import math

def guessin_game_function():
        name = input("Enter name: ")
        print("Welcome", name)

        random_number = random.randint(0,50)
        chances = math.log(50 - 0 +1, 2)
        print("Guess a number between 0 and 50\n You've got only", round(chances), "chances.")

        count = 0
        while count < chances:
            count += 1
            guess = int(input("Guess a number: "))
            if guess == random_number:
                print("You got it right after", count, "triew")
            if abs(guess - random_number) <= 10:
                print("Very Hot")
            elif abs(guess - random_number) <= 20:
              print("Hot")
            elif abs(guess - random_number) <= 30:
                print("Cold")
            else:
                print("Vey cold") 
        if count >= chances:
            print("Wrong! The answer is ", random_number)

guessin_game_function()

answer = input("Do you wish to play again? YES or NO: ")
while answer == "yes":
    answer.upper()
    guessin_game_function()
else:
    answer.upper()
    print("Thanks for playing. Please exit!")