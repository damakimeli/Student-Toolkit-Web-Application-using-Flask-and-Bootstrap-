from flask import Flask, jsonify, render_template

app = Flask(__name__)

# Home
@app.route('/')
def home():
    return render_template('home.html')

# About
@app.route('/about')
def about():
    return render_template('about.html')

# Contact
@app.route('/contact')
def contact():
    return render_template('contact.html')

# JSON APIs
@app.route('/api/user')
def user():
    return jsonify({"name": "Damaris", "role": "student"})

@app.route('/api/courses')
def courses():
    return jsonify({
        "courses": [
            {"name": "Python Basics", "status": "completed"},
            {"name": "Flask Web Development", "status": "in progress"}
        ]
    })

@app.route('/api/tasks')
def tasks():
    return jsonify({
        "tasks": [
            {"title": "Finish Flask project", "deadline": "2026-03-30"}
        ]
    })
    
from flask import request

tasks_list = []

@app.route('/add-task', methods=['GET', 'POST'])
def add_task():
    if request.method == 'POST':
        task = request.form.get('task')
        tasks_list.append(task)
        return "Task added! <a href='/'>Go Home</a>"

    return '''
        <form method="POST">
            <input type="text" name="task" placeholder="Enter task" required>
            <button type="submit">Add Task</button>
        </form>
    '''

if __name__ == '__main__':
    app.run(debug=True)