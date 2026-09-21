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

for items in task:
    print(items["title"], " - ", items["status"])



def view_task(task):
    for i in range(len(task)):
       
        print(f"{i + 1}. {task[i]['title']}\n Client: {task[i]['client']}\n Recipient: {task[i]['recipient']}\n Status: {task[i]['status']}\n Priority: {task[i]["priority"]}\n Due Date: {task[i]["due_date"]}")

view_task(task)    

def add_task(task):

    while True:  

        due_date = date.today()

        title = input("Enter Title: ")
        client = input("Enter Client: ")
        recipient = input("Enter Recipient: ")
        priority = input("Enter Priority: ")
        due_date = int(input("Enter Due Date yy/mm/dd: "))

        task_list = {
            "title": title,
            "client": client,
            "recipient": recipient,
            "priority": priority,
            "due_date": due_date
        }
        task.append(task_list)
        continue
    break


add_task(task)    

