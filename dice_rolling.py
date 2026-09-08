# Ask the user to roll the dice (y/n)
# If y
#  generate 2 random numbers
# If n
# print a thank you message 
# then terminate the program
# else
# If user enters somthing different
# print an invalid error message

import random

def dice_game():

 while True:
    number1 = random.randint(1, 6)
    number2 = random.randint(1, 6)



    select = input("Roll the dice y/n  \n").lower()
   

    if select == "y":
        print(f'{number1} and {number2}')    

    elif select == "n":
        print("Thank you for playing this game") 
        break    

 else:
        print("Invalid choice") 
dice_game()              

