import database
from flask import Flask, jsonify, request


app = Flask(__name__)

@app.route("/tasks", methods=["GET", "POST"])
def home():
    tasks = database.load_task_from_db()
    return jsonify(tasks) 

if __name__ == "__main__":
    app.run(debug=True)


