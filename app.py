import database
from flask import Flask, jsonify, request


app = Flask(__name__)


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
        if task_id is None:
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
    if tasks is None:
        return jsonify({
            "message": "failed to load task",
            "task": tasks
        }), 500
    elif tasks == []:
        return jsonify({
            "message": "Task list is empty",
            "tasks": tasks
        }), 200 
    else:
        return jsonify({
            "message": "Task successfully loaded",
            "task": tasks
        }), 200

@app.route("/tasks/<int:task_id>")
def get_task(task_id):
    tasks = database.get_task_from_db(task_id)
   
    if tasks is None:
        return jsonify({
            "message": "task_id not found",
            "task_id": task_id
        }),404
    elif tasks == []:
        return jsonify({
            "message": "task is empty",
            "task": tasks
        }),200
    else:
        return jsonify({
            "message": "id found successfully",
            "task": tasks
        }), 200

@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    task_to_del = database.delete_task_from_db(task_id)

    if task_to_del is None:
        return jsonify({
            "message": "task_id not found to delete",
            "task": task_id
        }), 404
    else:
            return jsonify({
                        "message": "task deleted successfully",
                        "task": task_id
                    }), 200

@app.route("/tasks/<int:task_id>", methods=["PATCH"])
def patch_task(task_id, status): 
    update = database.update_task_status_from_db(task_id, status)
    store = request.json          

if __name__ == "__main__":
    app.run(debug=True)


