import sqlite3



def get_connection():
    connection = sqlite3.connect("task.db")
    return connection  

def create_table():
    connection = get_connection()
    try:
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
    except sqlite3.Error as e:
        print(f"Database error8: {e}")
    finally:        
        connection.close()

def insert_task(title, client, recipient, priority, due_date):

    connection = get_connection()
    try:

        cursor = connection.execute(
            """
            INSERT INTO tasks
            (title, client, recipient, status, priority, due_date)
            VALUES(?, ?, ?, ?, ?, ?)
            """,
            (title, client, recipient, "Pending", priority, due_date))
        
        task_id = cursor.lastrowid
        connection.commit()
        return task_id

    except sqlite3.Error as e:
        print(f"Database error7: {e}")
        return None
    finally:        
        connection.close()

def load_task_from_db():
    connection = get_connection()
    store_dict = []

    try:
        select = connection.execute("SELECT * FROM tasks")
        rows = select.fetchall()

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
    except sqlite3.Error as e:
        print(f"Database error6: {e}")
    finally:            
        connection.close()
    
    return store_dict

def update_task_status_from_db(task_id, status):
    connection = get_connection()

    try:
        cursor = connection.execute("""
            UPDATE tasks
            SET status = ?
            WHERE id = ?
            """, (status, task_id))
        if cursor.rowcount == 0:
            print("Task not found")
            return None
        else:
            print("Task updated successfully")
            connection.commit()

            return True   
    except sqlite3.Error as e: 
        connection.rollback() 
        print(f"Database error4: {e}")
        return None
    finally:  
        connection.close()

def delete_task_from_db(task_id):
    connection = get_connection()
    try:
        cursor = connection.execute(
            """
            DELETE FROM tasks
            WHERE id = ?   
            """, (task_id,))
        if cursor.rowcount == 0:
            print("Task not found")
            return None
        else:
            print("Action successfully taken")
            connection.commit() 
            return True
    except sqlite3.Error as e:
        connection.rollback() 
        print(f"Database error2: {e}")
        return None
    finally:        
        connection.close() 

def clear_task_from_db():
    connection = get_connection()
    try:
        connection.execute("DELETE FROM tasks")
    
        connection.commit()
        return True
    except sqlite3.Error as e:
        connection.rollback()
        print(f"Database error3: {e}")
        return None
    finally:        
        connection.close()

def update_task_priority_from_db(task_id, priority):
    connection = get_connection()
    try:
        cursor = connection.execute(
            """
            UPDATE tasks
            SET priority = ?
            WHERE id = ?

            """, (priority, task_id))
        if cursor.rowcount == 0:
            print("Task not found")
            return None
        else:
            print("Task updated successfully")
            connection.commit()
            return True    

    except sqlite3.Error as e:
        connection.rollback()
        print(f"Database error5: {e}")
        return None 
    finally:       
        connection.close()


 