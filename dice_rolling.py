# Ask the user to roll the dice (y/n)
# If y
#  generate 2 random numbers
# If n
# print a thank you message 
# then terminate the program
# else
# If user enters somthing different
# print an invalid error messagey


import random

def dice_game():

 while True:
    number1 = random.randint(1, 6)
    number2 = random.randint(1, 6)

    
    try:
        select = input("Roll the dice y/n  ").lower()
        print("\n")
    except ValueError:
       print("Enter a valid input: y/n")    
   

    if select == "y":
        
        print(f'{number1} and {number2}') 
        if number1 == 6 and number2 == 6:
           print("Congratulations! you've hit jackpot")
           return


    elif select == "n":
        print("Thank you for playing this game") 
        break    

    else:
        print("Invalid choice") 
dice_game()              

