import database
from flask import Flask, jsonify, request, render_template


app = Flask(__name__)

@app.route("/")
def home2():
    return render_template("index.html")

@app.route("/tasks", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        if not request.is_json:
            return jsonify ({
                "message": "data must be json"
            }), 400
        try:
            data = request.json
            
            title = data["title"]
            client = data["client"]
            recipient = data["recipient"]
            priority = data["priority"]
            due_date = data["due_date"]
        except KeyError as error:
             
            return jsonify ({
                "message": "Field required",
                "field": error.args[0]
            }), 400  
        
        task_id = database.insert_task(title, client, recipient, priority, due_date)
        if task_id == "error":
            return jsonify({
                "message": "Failed to create task",
                "task_id": task_id
            }), 500
        else:
            return jsonify({
                "message": "Task successfully created", 
                "task_id": task_id
                }), 201
    tasks = database.load_task_from_db()
    if tasks == "error":
        return jsonify({
            "message": "failed to load task",
            "tasks": tasks
        }), 500
    elif tasks == []:
        return jsonify({
            "message": "Task list is empty",
            "tasks": tasks
        }), 200 
    else:
        return jsonify({
            "message": "Task successfully loaded",
            "tasks": tasks
        }), 200

@app.route("/tasks/<int:task_id>")
def get_task(task_id):
    tasks = database.get_task_from_db(task_id)
   
    if tasks == "not_found":
        return jsonify({
            "message": "task_id not found",
            "task_id": task_id
        }),404
    elif tasks == "error":
        return jsonify({
            "message": "Database error from task_id",
            "task_id": task_id
        }), 500
    else:
        return jsonify({
            "message": "id found successfully",
            "task": tasks
        }), 200

@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    task_to_del = database.delete_task_from_db(task_id)

    if task_to_del == "not_found":
        return jsonify({
            "message": "task_id not found to delete",
            "task_id": task_id
        }), 404
    elif task_to_del == "error":
        return jsonify({
            "message": "database deleting error",
            "task_id": task_id
        }), 500
    else:
        return jsonify({
            "message": "task deleted successfully",
            "task": task_id
        }), 200

@app.route("/tasks/<int:task_id>", methods=["PATCH"])
def patch_task(task_id): 
   
    if not request.is_json:
        return jsonify({
            "message": "data must be in json"
        }), 400
    try:
         data = request.json
         status = data["status"]             
    except KeyError as error:
          return jsonify ({
                "message": "Field required",
                "field": error.args[0]
            }), 400
    if status not in ["Pending", "Completed"]:
        return jsonify({
            "message": "Invalid input: select Pending or Completed.",

        }), 400
    

    update = database.update_task_status_from_db(task_id, status)    
    if update == "not_found":
          return jsonify ({
                "message": "id not found",
                "task_id": task_id
            }), 404
    elif update == "error":
        return jsonify ({
                "message": "database error",
                "task_id": task_id
            }), 500
    else:
         return jsonify({
              "message": "Status successfully updated",
              "status": status
         }), 200
@app.route("/tasks/<int:task_id>/priority", methods=["PATCH"])   
def patch_priority(task_id):
    if not request.is_json:
        return jsonify({
            "message": "Enter a valid json"
        }), 400
    try:
        data = request.json
        priorities = data["priority"]
    except KeyError as e:
        return jsonify ({
            "message": "Field required",
            "field": e.args[0]
        }), 400
    if priorities not in["High", "Medium", "Low"]:
         return jsonify ({
            "message": "Enter a valid input: High,Medium or Low",
            "task_id": task_id
        }), 400
    priority = database.update_task_priority_from_db(task_id, priorities)
    if priority == "not_found":
              return jsonify ({
                    "message": "id not found",
                    "task_id": task_id
                }), 404
    elif priority == "error":
        return jsonify ({
                "message": "database error while getting priority",
                "task_id": task_id
            }), 500
    else:
            return jsonify({
                "message": "priority successfully updated",
                "priorities": priorities
            }), 200


if __name__ == "__main__":
    app.run(debug=True, port=7000)


