# print a welcome message
#  Ask user to enter the name of the pruduct to be purchased
# Ask the user to enter the amount for the product
# Create a list and store the expense category
# Select the category of expenses from the list
# Create a while loop for the category selection

import csv
import json


def add_expense(expense):

    print("Welcome to expenses tracker \n")

    while True:

        add_expense = input("Do you want to add an expense? yes/no: ").lower()

        if add_expense == "yes":
            product_input = input("Enter your description: ")
            amount_input = float(input("Enter the amount: $"))
            print("\n")


            print("==LIST OF CATEGORIES==")
            expense_category = [
                "🍲Food",
                "🌆Work",
                "🤑Utilities",
                "🏠Rent",
                "🪁Fun",
                "📳Misceleneous"
            ]

            for i, value in enumerate(expense_category):
                print(f"{i + 1}. {value}")

            value = int(input("\n Select category: ")) - 1

            if value < 0 or value >= len(expense_category):
                print("Enter numer from 1-6")
                continue

            
            expenses = {
                "category": expense_category[value],
                "description":  product_input,
                "amount": amount_input


            }
            expense.append(expenses)

            print(f"Expense successfully added! {expense} \n")

        elif add_expense == "no":
            print("That will be all for now, thank you for using this tracker \n")
            break
        else:
            print('Invalid choice, Enter a valid choice yes/no')
    print("          ======SUMMARY=======        ")
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


print(f"Total Amount = {total_expense(expense)} \n")


def spend_by_category(expense):

    sort_category = {}

    for i in expense:
        if i["category"] in sort_category:
            sort_category[i["category"]] += i["amount"]
        else:
            sort_category[i["category"]] = i["amount"]

    return sort_category


print(f"Total of each category = {spend_by_category(expense)} \n")


def delete_expense():

    print("     ==SELECT EXPENSE TO REMOVE==     ")
    view_expenses(expense)
    while True:
        choice = int(input("Choose the expenses number to remove: ")) - 1
        if choice < 0 or choice >= len(expense):
            print("Enter a valid number.")
            continue
        break

    expense.pop(choice)
    print("Expenses successfully removed! \n")

    print("     ==REMAINING EXPENSE LIST==     ")
    view_expenses(expense)

    save_expenses(expense)

    return expense


delete_expense()

def jas_format(expense):

    print("\n         =====JSON FORMAT=====          ")


    
    for i in range(len(expense)):
       
        store = json.dumps(expense[i], ensure_ascii=False)

        print(f"{i + 1}. {store}")



jas_format(expense)

