


#INPUT
#input user guess
#PROCESSING
#loop while the user guess is incorrect
#OUTPUT
#message to user telling them too low, too high, or correct










import random

mynumber= random.randint(1, 10)
#Welcome user to the guessing game
print("Welcome to the guess the numbers game!/n")
userGuesses =[] #empty list
count = 1 #the count of incorrect guesses

#loop until correct guess
while True:
    try:
        guess = int(input("Please enter a number between 1 and 10: "))
    except ValueError:
        print("number only please!")
        continue
    userGuesses.append(guess) #add guess to the list
    if(guess<mynumber):
        print("Too Low")
        count +=1
    elif (guess>mynumber):
        print("Too High")
        count +=1
    elif (guess==mynumber):
        print("You guessed it! It took you", count," attempts")
        print("You picked the following numbers: ",userGuesses)
        break
















