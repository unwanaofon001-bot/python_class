import database
from flask import Flask
from falsk import jsonify

app = Flask(__name__)

@app.route("/tasks")
def home():
    tasks = database.load_task_from_db()
    return str(tasks)
    return jsonify(task) 

if __name__ == "__main__":
    print(app.url_map)
    app.run(debug=True)