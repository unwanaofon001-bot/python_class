from datetime import datetime
import database

task = []


def main():
    global task
    database.create_table()
    task = database.load_task_from_db()
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
                "Clear Task",
                "Exit"
            ]
        
        for i in range(len(manager)):
                print(f"{i + 1}. {manager[i]}")
        try:
            choice = int(input("\nchoose an option (1-7): ")) 
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
            clear_task()    
        elif choice == 7:
            print("Thank you for using this task manager")
            break
        else:
            print("invalid input: enter(1-7)")                  

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
                

                title = get_required_text("Title").title()
                client = get_required_text("Client").title()
                recipient = get_required_text("Recipient").title()
                priority = get_priority()
                due_date = get_due_date()

                
                task_id = database.insert_task(title, client, recipient, priority, due_date)
                if task_id is None:
                    print("Task could not be added to database")
                    return
                else:
                    new_list = create_task(task_id, title, client, recipient, priority, due_date)
                    task.append(new_list)
                    print(task)
              
            elif add_request == "n":
                print("Thank you for using this task manager \n") 
                break
            else:
                print("Invalid input: Enter y/n") 

def get_required_text(field_name):

    while True:
            user_input = input(f"Enter {field_name}: ").strip()
            if user_input == "":
                print(f"{field_name} cannot be empty")
                continue
            return user_input

def create_task(task_id, title, client, recipient, priority, due_date):
   

    task_list = {
        "id": task_id,
        "title": title,
        "client": client,
        "recipient": recipient,
        "status": "Pending",
        "priority": priority,
        "due_date": due_date
    }    
    return task_list
       
def completed_task():

    view_task(task) 
     
    if not task:
        print("No task to complete at the moment")
        return
   
    complete_choice = get_index(task)   
    print("\n")
        
    if task[complete_choice]["status"] == "Pending":
        updated = database.update_task_status_from_db(task[complete_choice]["id"], "Completed") 
        if updated == True:
            task[complete_choice]["status"] = "Completed"         
    else: 
        print("Task is already completed \n")    
 
    view_task(task)
    
def change_priority():

    view_task(task)

    if not task:
        print("No task to complete at the moment")
        return

    task_choice = get_index(task)

    print("\n")
        
    while True:   
        change = input("Enter new priority: ").lower()
        if change in["high", "medium", "low"]:
            change = change.capitalize()
            updated = database.update_task_priority_from_db(task[task_choice]["id"], change )
            if updated == True:
                task[task_choice]["priority"] = change
                print("Priority added successfully\n")
            else:
                print("Fail to update priority")    

        else:
            print("Invalid priority, choose (high, medium or low)")
            continue
        break

    view_task(task)   

def delete_task():

    if not task:
        print("No task to complete at the moment")
        return
    
    print("=" *10)
    print("|  LIST  |")
    print("=" *10)
    view_task(task)

    remove = get_index(task)

    while True: 
        recheck = input("Are you sure you want to delete this task? y/n: ").lower()
        if recheck == "y":
            task_id = task[remove]["id"]
            delete = database.delete_task_from_db(task_id)
            if delete == True:
                task.pop(remove)
                print("You have successfully deleted a task \n")
            else:
                print("failed to delete task")    
                return None
        elif recheck == "n":
            print("Okay, now select the right task to delete \n")    
            return
        else:            
            print("Invalid input: Enter y/n \n")
            
            
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

def get_due_date():

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
            return due_date

def get_index(task):
    while True:
        try:
            store_idx = int(input("Enter number: ")) -1
        except ValueError:
            print("invalid Input")
            continue  

        if store_idx < 0 or store_idx >= len(task):
            print("Number out of range")
            continue
        return store_idx

def clear_task():
        if not task:
            print("No task to complete at the moment")
            return
        
        print("=" *10)
        print("|  LIST  |")
        print("=" *10)
        view_task(task)
    
        while True: 
            recheck = input("Are you sure you want to clear this list? y/n: ").lower()
            if recheck == "y":
                cleared = database.clear_task_from_db()
                if cleared == True:
                    task.clear()
                    print("You have successfully cleared the list \n")
                else:
                    print("Failed to clear list")    
                break
            elif recheck == "n":
                print("Okay, cleared selection is cancelled \n")    
                return
            else:            
                print("Invalid input: Enter y/n \n")
                        
        print("=" *35)
        print("|    TASK LIST AFTER DELETE      |")
        print("=" *35)
    
        view_task(task)

if __name__ == "__main__":
    main()

