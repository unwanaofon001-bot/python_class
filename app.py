import database
from flask import Flask, jsonify, request


app = Flask(__name__)

@app.route("/tasks", methods=["GET", "POST"])
def home():
    if request.method == "POST":
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
    return jsonify(tasks) 

if __name__ == "__main__":
    app.run(debug=True)


