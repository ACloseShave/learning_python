#############################
##  Guess the Number Game  ##
#############################

#Importing the random function
import random


number_answer = random.randrange(1,1000)                                          #limit the range of numbers
guess_counter = 1                                                                 #counter off-by-1 error


print("Hello! Let's play a game.")

play_game = 'y'                                                                   #game repeat control default value

while play_game == 'y':
    print("I'm thinking of a number between 1 and 1000.")
    player_guess = int(input("What do you think the number is? "))                #player initial guess

    while player_guess != number_answer:                                          #first guess wrong loop
        if 1 <= player_guess and player_guess <= 1000:                            #constraining inputs
            if player_guess < number_answer:
                player_guess = int(input("Too low! Try again: "))                 #guess is too low
            elif player_guess > number_answer:
                player_guess = int(input("Too high! Guess again: "))              #guess is too high
            guess_counter += 1
        else:
            print("Oops! That number isn't between 1 and 1000")
            player_guess = int(input("Try again: "))                              #guess outside constraint range
            guess_counter += 1

    print("That's correct! It took you", guess_counter, "tries to guess it!")

    play_game = input("Do you want to play again? Type 'y' for another game: ")   #game repeat control
    if play_game == 'y':
        number_answer = random.randrange(1,1000)                                  #generate new number for new game
        guess_counter = 1 
