from flask import Flask, request, jsonify
import psycopg2

app = Flask(__name__)

# Connect to PostgreSQL (use env vars in real apps)
conn = psycopg2.connect(
    host="your-db-host",
    database="your-db-name",
    user="your-db-user",
    password="your-db-password"
)
cur = conn.cursor()

# Create table if not exists
cur.execute("""
CREATE TABLE IF NOT EXISTS tasks (
    id SERIAL PRIMARY KEY,
    title TEXT NOT NULL
)
""")
conn.commit()

# Route: Home
@app.route('/')
def home():
    return "Task Manager API running!"

# Route: Add a task
@app.route('/tasks', methods=['POST'])
def add_task():
    title = request.json['title']
    cur.execute("INSERT INTO tasks (title) VALUES (%s) RETURNING id", (title,))
    task_id = cur.fetchone()[0]
    conn.commit()
    return jsonify({'id': task_id, 'title': title})

# Route: View all tasks
@app.route('/tasks', methods=['GET'])
def get_tasks():
    cur.execute("SELECT id, title FROM tasks")
    tasks = [{'id': row[0], 'title': row[1]} for row in cur.fetchall()]
    return jsonify(tasks)

# Route: Delete a task
@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    cur.execute("DELETE FROM tasks WHERE id = %s", (task_id,))
    conn.commit()
    return jsonify({'message': f'Task {task_id} deleted'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
