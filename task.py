from datetime import datetime

task = []


def main():
    task_manager()
    

def task_manager():
   
    while True:
        print('=' *25)
        print("      TASK MANAGER      ")
        print('=' *25)
        
        manager = [
                "View task",
                "Add task",
                "Completed Task",
                "Change Priority",
                "Delete Task",
                "Exit"
            ]
        
        for i in range(len(manager)):
                print(f"{i + 1}. {manager[i]}")
        try:
            choice = int(input("\nchoose an option (1-6): ")) 
        except ValueError:
            print("Enter a number") 
            continue   
        print("\n")

        if choice == 1:
            view_task(task)
        elif choice == 2:
            add_task(task)
        elif choice == 3:
            completed_task()
        elif choice == 4:
            change_priority()     
        elif choice == 5:
            delete_task()
        elif choice == 6:
            print("Thank you for using this task manager")
            break
        else:
            print("invalid input: enter(1-6)")                  

def view_task(task):
    if len(task) == 0:
        print("\nTask not available \n")
    else:    
        for i in range(len(task)):
       
            print(f"{i + 1}. {task[i]['title']}\n"
                f"Client: {task[i]['client']}\n"
                f"Recipient: {task[i]['recipient']}\n" 
                f"Status: {task[i]['status']}\n"
                f"Priority: {task[i]['priority']}\n"
                f"Due Date: {task[i]['due_date']}\n")
    

def add_task(task):
    print("=" *25)
    print("        ADD TASK        ")
    print("=" *25)

    while True: 
            print("\n")
            add_request = input("Do you want to add task? y/n: ").lower()
            print("\n")

            if add_request == "y":

                while True:
                    title = input("Enter Title: ").strip()
                    if title == "":
                        print("Title cannot be empty")
                        continue
                    break
                while True:    
                    client = input("Enter Client: ").strip()
                    if client == "":
                        print("Client cannot be empty")
                        continue
                    break
                while True:
                    recipient = input("Enter Recipient: ").strip()
                    if recipient == "":
                        print("Recipient cannot be empty")
                        continue
                    break
                while True:  
                    due_date = (input("Enter Due Date dd-mm-yyyy: ")).strip()
                    if due_date == "":
                        print("Due Date cannot be empty")
                        continue
                    try:      
                        datetime.strptime(due_date,"%d-%m-%Y")
                    except ValueError:        
                        print("Invalid input: Enter dd-mm-yyyy")
                        continue
                    break    

                task_list = {
                    "title": title,
                    "client": client,
                    "recipient": recipient,
                    "status": "Pending",
                    "priority": get_priority(),
                    "due_date": due_date
                }

                task.append(task_list)
            elif add_request == "n":
                print("Thank you for using this task manager \n") 
                break
            else:
                print("Invalid input: Enter y/n")             

def completed_task():

    view_task(task) 
     
    if not task:
        print("No task to complete at the moment")
        return

    while True:
        
        try:
            complete_choice = int(input("Enter the number of the completed task: ")) -1
        except ValueError:
            print("Enter a valid number") 
            continue    
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

def change_priority():

    view_task(task)

    if not task:
        print("No task to complete at the moment")
        return


    while True:
        try:
            task_choice = int(input("Enter the number to change the priority: ")) -1 
        except ValueError:
            print("Enter a valid number")
            continue
        print("\n")
        
        if task_choice < 0 or task_choice >= len(task):
         print("Number out of range")    
         continue
          
        change = input("Enter new priority: ").lower()
        if change in["high", "medium", "low"]:
            change = change.capitalize()
            task[task_choice]["priority"] = change
        else:
            print("Invalid priority, choose (high, medium or low)")
            continue
        break
    print("Priority added successfully\n")

    view_task(task) 
          

def delete_task():

    if not task:
        print("No task to complete at the moment")
        return
    
    print("=" *10)
    print("|  LIST  |")
    print("=" *10)
    view_task(task)

    while True: 

        try:
            remove = int(input("Select task to delete: ")) -1
        except ValueError:
            print("Enter a number")
            continue

        if remove  < 0 or remove >= len(task):
            print("Enter number within range\n")
            continue
  

        recheck = input("Are you sure you want to delete this task? y/n: ").lower()
        if recheck == "y":
            task.pop(remove)
            print("You have successfully deleted a task \n")
            break
        elif recheck == "n":
            print("Okay, now select the right task to delete \n")
        else:            
            print("Invalid input: Enter y/n \n")
            continue
           
    print("=" *35)
    print("|    TASK LIST AFTER DELETE      |")
    print("=" *35)

    view_task(task)

def get_priority():

     while True:
            priority = input("Enter Priority: ").strip()
            if priority == "":
                print("Priority cannot be empty")
                continue
            if priority in["high", "medium", "low"]:
                priority = priority.capitalize()
            else:
                print("Invalid priority, choose (high, medium or low)")
                continue
            return priority


main()

