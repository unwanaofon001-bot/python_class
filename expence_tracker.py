# print a welcome message
#  Ask user to enter the name of the pruduct to be purchased
# Ask the user to enter the amount for the product
# Create a list and store the expense category
# Select the category of expenses from the list 
# Create a while loop for the category selection
def expense_track():

    print("Welcome to expenses tracker")

    expense_category = {
        "🍲Food": [],
        "🌆Work": [],
        "🤑Utilities": [],
        "🏠Rent": [],
        "🪁Fun": [],
        "📳Misceleneous": []
    }



    while True:

        add_expense = input("Do you want to add an expense? yes/no: ").lower()
        

        if add_expense == "yes":
            product_input = input("Enter your expense: ")
            amount_input = float(input("Enter the amount: $"))

                           
            for i, value in enumerate(expense_category):
             print(f"{i + 1}. {value}")

                
            value = int(input("Select category: ")) -1
            
            print(f"You have added ({product_input} = {amount_input}) to your expense list")
            
           
        elif add_expense == "no":
            print("That will be all for now, thank you for using this tracker")
            break 
        else:
            print('Invalid choice, Enter yes/no')


expense_track()  

def expense_table(product_input, amount_input):

    total_amount = sum(amount_input)
    display = {
        "category"
    }
    
    print(f"{product_input} = {amount_input}")
    
    




