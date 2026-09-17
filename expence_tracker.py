# print a welcome message
#  Ask user to enter the name of the pruduct to be purchased
# Ask the user to enter the amount for the product
# Create a list and store the expense category
# Select the category of expenses from the list 
# Create a while loop for the category selection

import csv


def add_expense(expense):

    print("Welcome to expenses tracker")

    


    while True:

        add_expense = input("Do you want to add an expense? yes/no: ").lower()
        

        if add_expense == "yes":
            product_input = input("Enter your description: ")
            amount_input = float(input("Enter the amount: $"))

            expense_category = [
                    "🍲Food",
                    "🌆Work",
                    "🤑Utilities",
                    "🏠Rent",
                    "🪁Fun",
                    "📳Misceleneous",
                ]
            
                           
            for i, value in enumerate(expense_category):
              print(f"{i + 1}. {value}")

                     
            value = int(input("Select category: ")) - 1

            if value < 0 or value >= len(expense_category):
                    print("Enter numer from 1-6")
                    continue

        

            expenses = {
                "category": expense_category[value],
                "description": product_input,
                "amount": amount_input
               
                
                                                }
            expense.append(expenses)
            
            
            print(f"Expenses successfully added! {expense}")
            
           
        elif add_expense == "no":
            print("That will be all for now, thank you for using this tracker")
            break 
        else:
            print('Invalid choice, Enter a valid choice yes/no')

           
            

expense = [] 


add_expense(expense)



def save_expenses(expense):


    with open("expense.csv", "w", newline="", encoding="utf-8") as file:

        sectionames = ["category", "description", "amount"]

        writer = csv.DictWriter(file, fieldnames=sectionames)

        writer.writeheader()

        writer.writerows(expense)

save_expenses(expense)


def load_expenses():
    # df = pd.read_csv('expense.csv', dtype={'amount': int, 'category': str, 'description': str})

     #expenses = []
     expenses = load_expenses()
 

     add_expense(expense)

     save_expenses(expense)

     
     with open("expense.csv", "r", newline="", encoding="utf-8") as file:
         reader = csv.DictReader(file)

         for row in reader:
            row["amount"] = float(row["amount"])
                   

            expenses.append(row)


        
     return expenses 


def view_expenses(expense):

     for i, store in enumerate(expense):



        print(f"{i + 1}. {store}")
    

view_expenses(expense)   


def total_expense(expense):

    total = 0

    for i in expense:

      
         total += i["amount"]
    return total  
   
print(f"Total Expenditure = {total_expense(expense)}")  


def spend_by_category(expense):

    sort_category = {}

    for i in expense:
        sort_category += expense["category"]
        if expense["category"] == sort_category:
            








    





        




         
   







   


        





 












# def delete_expense():


        




    
    




