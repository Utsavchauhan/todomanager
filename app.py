from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import sqlite3
import os
from datetime import datetime
from typing import Optional, List, Dict

app = Flask(__name__)
CORS(app)  # Enable CORS for API requests

# Database file path
DB_PATH = 'data/todo_manager.db'

def get_db_connection():
    """Get database connection"""
    # Ensure data directory exists
    os.makedirs('data', exist_ok=True)
    
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row  # Return rows as dictionaries
    return conn

def init_database():
    """Initialize database schema"""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Create todos table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS todos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            frequency TEXT NOT NULL CHECK(frequency IN ('daily', 'weekly', 'monthly', 'yearly')),
            status TEXT NOT NULL DEFAULT 'open' CHECK(status IN ('open', 'in_progress', 'completed')),
            goal_date TEXT,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Create trigger to update updated_at timestamp
    cursor.execute('''
        CREATE TRIGGER IF NOT EXISTS update_todos_timestamp 
        AFTER UPDATE ON todos
        BEGIN
            UPDATE todos SET updated_at = CURRENT_TIMESTAMP WHERE id = NEW.id;
        END
    ''')
    
    # Create indexes
    cursor.execute('CREATE INDEX IF NOT EXISTS idx_status ON todos(status)')
    cursor.execute('CREATE INDEX IF NOT EXISTS idx_frequency ON todos(frequency)')
    cursor.execute('CREATE INDEX IF NOT EXISTS idx_goal_date ON todos(goal_date)')
    
    conn.commit()
    conn.close()
    print(f"Database initialized at: {DB_PATH}")

# Initialize database on startup
init_database()

@app.route('/')
def index():
    """Serve the main HTML page"""
    return render_template('index.html')

@app.route('/api/todos', methods=['GET'])
def get_all_todos():
    """Get all todos"""
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM todos ORDER BY created_at DESC')
        todos = cursor.fetchall()
        conn.close()
        
        # Convert rows to dictionaries
        todos_list = [dict(todo) for todo in todos]
        return jsonify(todos_list), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/todos/<int:todo_id>', methods=['GET'])
def get_todo(todo_id):
    """Get a specific todo by ID"""
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM todos WHERE id = ?', (todo_id,))
        todo = cursor.fetchone()
        conn.close()
        
        if todo:
            return jsonify(dict(todo)), 200
        else:
            return jsonify({'error': 'Todo not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/todos', methods=['POST'])
def create_todo():
    """Create a new todo"""
    try:
        data = request.get_json()
        
        # Validate required fields
        if not data or 'title' not in data or 'frequency' not in data:
            return jsonify({'error': 'Title and frequency are required'}), 400
        
        title = data['title']
        description = data.get('description', '')
        frequency = data['frequency']
        status = data.get('status', 'open')
        goal_date = data.get('goalDate') or data.get('goal_date')
        
        # Validate frequency
        if frequency not in ['daily', 'weekly', 'monthly', 'yearly']:
            return jsonify({'error': 'Invalid frequency'}), 400
        
        # Validate status
        if status not in ['open', 'in_progress', 'completed']:
            return jsonify({'error': 'Invalid status'}), 400
        
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO todos (title, description, frequency, status, goal_date)
            VALUES (?, ?, ?, ?, ?)
        ''', (title, description, frequency, status, goal_date))
        
        todo_id = cursor.lastrowid
        conn.commit()
        conn.close()
        
        # Return the created todo
        return get_todo(todo_id)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/todos/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    """Update an existing todo"""
    try:
        data = request.get_json()
        
        if not data:
            return jsonify({'error': 'No data provided'}), 400
        
        conn = get_db_connection()
        cursor = conn.cursor()
        
        # Check if todo exists
        cursor.execute('SELECT * FROM todos WHERE id = ?', (todo_id,))
        if not cursor.fetchone():
            conn.close()
            return jsonify({'error': 'Todo not found'}), 404
        
        # Build update query dynamically
        updates = []
        values = []
        
        if 'title' in data:
            updates.append('title = ?')
            values.append(data['title'])
        if 'description' in data:
            updates.append('description = ?')
            values.append(data.get('description', ''))
        if 'frequency' in data:
            if data['frequency'] not in ['daily', 'weekly', 'monthly', 'yearly']:
                conn.close()
                return jsonify({'error': 'Invalid frequency'}), 400
            updates.append('frequency = ?')
            values.append(data['frequency'])
        if 'status' in data:
            if data['status'] not in ['open', 'in_progress', 'completed']:
                conn.close()
                return jsonify({'error': 'Invalid status'}), 400
            updates.append('status = ?')
            values.append(data['status'])
        if 'goalDate' in data or 'goal_date' in data:
            goal_date = data.get('goalDate') or data.get('goal_date')
            updates.append('goal_date = ?')
            values.append(goal_date)
        
        if not updates:
            conn.close()
            return jsonify({'error': 'No fields to update'}), 400
        
        values.append(todo_id)
        query = f'UPDATE todos SET {", ".join(updates)} WHERE id = ?'
        
        cursor.execute(query, values)
        conn.commit()
        conn.close()
        
        # Return the updated todo
        return get_todo(todo_id)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    """Delete a todo"""
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        
        # Check if todo exists
        cursor.execute('SELECT * FROM todos WHERE id = ?', (todo_id,))
        if not cursor.fetchone():
            conn.close()
            return jsonify({'error': 'Todo not found'}), 404
        
        cursor.execute('DELETE FROM todos WHERE id = ?', (todo_id,))
        conn.commit()
        conn.close()
        
        return jsonify({'message': 'Todo deleted successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# For production deployment, use: gunicorn app:app
# The app variable is the WSGI application
# For local development, you can still run: python app.py (but it won't start server)

