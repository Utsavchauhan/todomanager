# How to Access SQLite Database

## Database Location
The SQLite database file is located at:
```
data/todo_manager.db
```

## Method 1: Command Line (sqlite3)

### Connect to the database:
```bash
sqlite3 data/todo_manager.db
```

### Useful SQLite Commands:

Once connected, you can use these commands:

```sql
-- View all tables
.tables

-- View table structure
.schema todos

-- View all todos
SELECT * FROM todos;

-- View todos with formatted output
.mode column
.headers on
SELECT * FROM todos;

-- View specific columns
SELECT id, title, status, frequency FROM todos;

-- Count todos
SELECT COUNT(*) FROM todos;

-- View todos by status
SELECT * FROM todos WHERE status = 'open';

-- View todos by frequency
SELECT * FROM todos WHERE frequency = 'daily';

-- Exit sqlite3
.quit
```

### Quick Commands (without entering interactive mode):

```bash
# View all todos
sqlite3 data/todo_manager.db "SELECT * FROM todos;"

# View todos with headers
sqlite3 data/todo_manager.db -header -column "SELECT * FROM todos;"

# Count todos
sqlite3 data/todo_manager.db "SELECT COUNT(*) FROM todos;"

# View table schema
sqlite3 data/todo_manager.db ".schema todos"
```

## Method 2: Python Script

Create a Python script to access the database:

```python
import sqlite3

# Connect to database
conn = sqlite3.connect('data/todo_manager.db')
cursor = conn.cursor()

# Execute queries
cursor.execute("SELECT * FROM todos")
todos = cursor.fetchall()

for todo in todos:
    print(todo)

# Close connection
conn.close()
```

## Method 3: GUI Tools

### DB Browser for SQLite (Recommended)
- Download: https://sqlitebrowser.org/
- Open the app
- Click "Open Database"
- Navigate to `data/todo_manager.db`
- Browse and edit data visually

### VS Code Extension
- Install "SQLite Viewer" extension in VS Code
- Right-click on `data/todo_manager.db`
- Select "Open Database"

### DBeaver (Universal Database Tool)
- Download: https://dbeaver.io/
- Create new connection → SQLite
- Browse to `data/todo_manager.db`

## Method 4: Online SQLite Viewer
- Upload `data/todo_manager.db` to: https://sqliteviewer.app/
- View and query your database online

## Common Queries

### View all todos:
```sql
SELECT * FROM todos ORDER BY created_at DESC;
```

### View todos by status:
```sql
SELECT * FROM todos WHERE status = 'open';
SELECT * FROM todos WHERE status = 'in_progress';
SELECT * FROM todos WHERE status = 'completed';
```

### View todos by frequency:
```sql
SELECT * FROM todos WHERE frequency = 'daily';
SELECT * FROM todos WHERE frequency = 'weekly';
SELECT * FROM todos WHERE frequency = 'monthly';
SELECT * FROM todos WHERE frequency = 'yearly';
```

### Statistics:
```sql
-- Count by status
SELECT status, COUNT(*) as count FROM todos GROUP BY status;

-- Count by frequency
SELECT frequency, COUNT(*) as count FROM todos GROUP BY frequency;

-- Todos with upcoming goal dates
SELECT * FROM todos WHERE goal_date IS NOT NULL AND goal_date >= date('now') ORDER BY goal_date;
```

### Update data:
```sql
-- Update todo status
UPDATE todos SET status = 'completed' WHERE id = 1;

-- Update todo title
UPDATE todos SET title = 'New Title' WHERE id = 1;

-- Delete a todo
DELETE FROM todos WHERE id = 1;
```

## Backup Database

```bash
# Copy the database file
cp data/todo_manager.db data/todo_manager_backup.db

# Or use sqlite3 backup command
sqlite3 data/todo_manager.db ".backup data/todo_manager_backup.db"
```

## Reset Database

```bash
# Delete the database file (will be recreated on next app run)
rm data/todo_manager.db
```

