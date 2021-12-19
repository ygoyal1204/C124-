from flask import Flask, jsonify, request

app = Flask(__name__)
tasks = [
    {
        "id": 1,
        "title": "Buy Groceries",
        "description": "milk, cheese, pizza, fruit",
        "done": False
    },
    {
        "id": 2,
        "title": "Learn Python",
        "description": "You need to find a python tutorial on the web",
        "done": False
    }
]
@app.route("/")

@app.route("/add-data", methods=["POST"])

def add_task():
    if not request.json:
        return jsonify({
            "status": "error",
            "message": "please provide the data"
        }, 400)
    task = {
        "id": tasks[-1]["id"]+1,
        "title": request.json["title"],
        "description": request.json.get("description", ""),
        "done": False
    }

    tasks.append(task)
    return jsonify({
        "status": "Success",
        "message": "Task added successfully"
    })

@app.route("/get-data", methods=["POST"])

def get_task():
    return jsonify({
        "data": tasks
    })

if __name__ == "__main__":
    app.run(debug=True)



