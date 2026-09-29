from datetime import datetime
import sqlite3
connection = sqlite3.connect("task.db")

task = []


def main():
    global task
    task = load_task_from_db()
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

                new_list = create_task(title, client, recipient, priority, due_date)
                task.append(new_list)
              
                insert_task(title, client, recipient, priority, due_date)

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

def create_task(title, client, recipient, priority, due_date):
   

    task_list = {

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
        task[complete_choice]["status"] = "Completed"
        update_task_status(task[complete_choice]["id"], "Completed")
        
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
            task[task_choice]["priority"] = change
            updated_priority = task[task_choice]["priority"]
            update_task_priority_from_db(task[task_choice]["id"], updated_priority )
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

    remove = get_index(task)

    while True: 
        recheck = input("Are you sure you want to delete this task? y/n: ").lower()
        if recheck == "y":
            task_id = task[remove]["id"]
            task.pop(remove)
            delete_task_from_db(task_id)
            print("You have successfully deleted a task \n")
            break
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
                task.clear()
                clear_task_from_db()
                print("You have successfully cleared the list \n")
                break
            elif recheck == "n":
                print("Okay, now select the right task to delete \n")    
                return
            else:            
                print("Invalid input: Enter y/n \n")
                        
        print("=" *35)
        print("|    TASK LIST AFTER DELETE      |")
        print("=" *35)
    
        view_task(task)


connection.execute("""
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        client TEXT,
        recipient TEXT,
        status TEXT,
        priority TEXT,
        due_date TEXT
    )

""")
connection.commit()

def insert_task(title, client, recipient, priority, due_date):

    connection.execute(
        """
        INSERT INTO tasks
        (title, client, recipient, status, priority, due_date)
        VALUES(?, ?, ?, ?, ?, ?)
        """,
        (title, client, recipient, "Pending", priority, due_date))
    connection.commit()

def load_task_from_db():
    select = connection.execute("SELECT * FROM tasks")
    rows = select.fetchall()

    store_dict = []

    for i in rows:
        task_dict = {
            "id": i[0],
            "title": i[1],
            "client": i[2],
            "recipient": i[3],
            "status": i[4],
            "priority": i[5],
            "due_date": i[6]
        }
        store_dict.append(task_dict)
    
    return store_dict

def update_task_status(task_id, status):
    connection.execute("""
        UPDATE tasks
        SET status = ?
        WHERE id = ?
        """, (status, task_id))
    connection.commit()

def delete_task_from_db(task_id):
    connection.execute(
        """
         DELETE FROM tasks
         WHERE id = ?   
        """, (task_id,))
    connection.commit()   

def clear_task_from_db():
    connection.execute("DELETE FROM tasks")
    connection.commit()

def update_task_priority_from_db(task_id, priority):
    connection.execute(
        """
        UPDATE tasks
        SET priority = ?
        WHERE id = ?

        """, (priority, task_id))
    connection.commit()

    


main()

