# number guessing game using if and conditionals

# generate random number between 1 and 100
import random
target = random.randint(0, 100)
give_up = False
times_guessed = 0
print(target)
# get user to guess the number
guess = int(input("Guess which number between 1 and 100 I'm thinking of: "))
times_guessed += 1
# if incorrect, loop until user guesses correct number
while guess != target:
    # counts how many guesses the user has had and informs them of option to quit after 3 tries
    if times_guessed == 3:
        print("If you want to quit just pick a number outside of the range")
    #if user gives up then break
    if guess < 0 or guess > 100:
        give_up = True
        break
    # if guess too high then tell them and get new guess
    elif guess > target:
        guess = int(input("Too high, try again: "))
        times_guessed += 1
    # otherwise guess must be too low so tell them and get new guess
    else:
        guess = int(input("Too low, try again: "))
        times_guessed += 1
# guess is now correct or player quit so provide appropriate ending message
print("Outside of range. Sorry to see you go :(") if give_up else print(f"Well done, you got it in {times_guessed} attempts!!")
