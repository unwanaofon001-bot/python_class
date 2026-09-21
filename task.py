from datetime import date 

task = [
    { 
      "title": "Weekly Sales Report",
      "client": "ABC company",
      "recipient": "The Manager",
      "status": "Pending",
      "priority": "High",
      "due_date": "20-09-2026"
    },
 
    { 
      "title": "Daily Sales Report",
      "client": "Food company",
      "recipient": "The HR",
      "status": "Pending",
      "priority": "High",
      "due_date": "21-09-2026"
    },
 
    { 
      "title": "Monthly Sales Report",
      "client": "Tax company",
      "recipient": "The Manager",
      "status": "Completed",
      "priority": "High",
      "due_date": "23-09-2026"
    }
]

for items in range(len(task)):
    print(f"{items + 1}. {task[items]}")
    print("\n")




def view_task(task):
    for i in range(len(task)):
       
        print(f"{i + 1}. {task[i]['title']}\n"
            f"Client: {task[i]['client']}\n"
            f"Recipient: {task[i]['recipient']}\n" 
            f"Status: {task[i]['status']}\n"
            f"Priority: {task[i]["priority"]}\n"
            f"Due Date: {task[i]["due_date"]}\n")

view_task(task)    

def add_task(task):
    print("========================")
    print("        ADD TASK        ")
    print("========================")

    while True: 
        print("\n")
        add_request = input("Do you want to add task? y/n: ").lower()
        print("\n")


        if add_request == "y":

            title = input("Enter Title: ")
            client = input("Enter Client: ")
            recipient = input("Enter Recipient: ")
            priority = input("Enter Priority: ")
            due_date = (input("Enter Due Date dd-mm-yy: "))
            print("\n")

            task_list = {
                "title": title,
                "client": client,
                "recipient": recipient,
                "status": "Pending",
                "priority": priority,
                "due_date": due_date
            }
            task.append(task_list)
        elif add_request == "n":
            print("Thank for using this task manager \n") 
            break
        else:
            print("Invalid input: Enter y/n")  
           
         

add_task(task)  


def completed_task():

    view_task(task)  

    while True:
        complete_choice = int(input("Enter the task number to complete: ")) -1 
        print("\n")

        if complete_choice < 0 or complete_choice >= len(task):
            print("Enter number within range")    
            continue
        break



    if task[complete_choice]["status"] == "Pending":
        task[complete_choice]["status"] = "Completed"
    else:
        print("Task is already completed \n")    

        
    view_task(task)
  
            
completed_task()        


def delete_task():
    print("==========")
    print("|  LIST  |")
    print("==========")
    view_task(task)
    while True: 

        remove = int(input("Select task to delete: ")) -1
        if remove  < 0 or remove >= len(task):
            print("Enter number within range")
            continue

    

        recheck = input("Are you sure you want to delete this task? y/n: ").lower()
        if recheck == "y":
            task.pop(remove)
            print("You have successfully removed the task \n")
            break
        elif recheck == "n":
            print("Okay, now select the correct task \n")
        else:            
            print("Invalid input: Enter y/n \n")
            continue
           
                    

    print("==================================")
    print("|    TASK LIST AFTER DELETE      |")
    print("==================================")
    print("\n")

    view_task(task)


delete_task()






