# number guessing game using if statements

# generate random number between 1 and 100
import random
target = random.randint(0, 101)
print(target)
# get user to guess the number
guess = int(input("Guess which number between 1 and 100 I'm thinking of: "))
# if incorrect, loop until user guesses correct number
while guess != target:
    # if guess too high then tell them and get new guess
    if guess > target:
        guess = int(input("Too high, try again: "))
    # if guess is too low then tell them and get new guess
    elif guess < target:
        guess = int(input("Too low, try again: "))
# guess is correct so victory message
print("Well done, you got it!!")