# Ask the user to guess a number
# check if the guessed number is the same as the random number
# if the guess number is lower than the result
# print a message that the number is too low
# else
#


import random

def guessing_game():

    number = random.randint(1, 100)
   

    while True: 

     guessed_number = int(input('Enter a random number: '))

    if guessed_number > number:
       print("Too high, enter a lower number")
    elif guessed_number < number:
       print('Too low, enter a higher number')
    else:
       print('Congratulations, You got it 🎉🎉')
       #break
        
 

guessing_game()       

