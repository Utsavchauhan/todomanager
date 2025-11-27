# Todo Manager - Python Edition

A simple Todo List Manager application built with Python Flask, SQLite, and HTML/CSS/JavaScript.

## Features

- ✅ Create todos with different frequencies (Daily, Weekly, Monthly, Yearly)
- ✅ Track todo status (Open, In Progress, Completed)
- ✅ Set goal dates for todos
- ✅ Update todo status
- ✅ Delete todos
- ✅ Beautiful, responsive UI
- ✅ **Zero configuration** - SQLite database is created automatically!

## Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

## Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Run the Application

```bash
python app.py
```

The application will start on `http://localhost:5000`

**That's it!** The SQLite database will be created automatically in the `data/` directory when you first run the application.

## Project Structure

```
Todo Manager/
├── app.py                 # Flask application and API endpoints
├── requirements.txt       # Python dependencies
├── templates/
│   └── index.html        # Frontend HTML/CSS/JavaScript
├── data/                 # SQLite database (created automatically)
│   └── todo_manager.db
└── README.md
```

## API Endpoints

### GET `/api/todos`
Get all todos

**Response:**
```json
[
  {
    "id": 1,
    "title": "Example Todo",
    "description": "This is an example",
    "frequency": "daily",
    "status": "open",
    "goal_date": "2024-12-31",
    "created_at": "2024-11-26 15:00:00",
    "updated_at": "2024-11-26 15:00:00"
  }
]
```

### GET `/api/todos/{id}`
Get a specific todo by ID

### POST `/api/todos`
Create a new todo

**Request Body:**
```json
{
  "title": "Example Todo",
  "description": "This is an example",
  "frequency": "daily",
  "status": "open",
  "goalDate": "2024-12-31"
}
```

### PUT `/api/todos/{id}`
Update an existing todo

**Request Body:**
```json
{
  "status": "in_progress"
}
```

### DELETE `/api/todos/{id}`
Delete a todo

## Database

The application uses **SQLite**, which means:
- ✅ No database server setup required
- ✅ Database file is created automatically at `data/todo_manager.db`
- ✅ Perfect for development and testing
- ✅ Easy to backup (just copy the .db file)
- ✅ Zero configuration

The database schema is automatically created when the application starts for the first time.

## Development

### Running in Development Mode

The app runs in debug mode by default:
```bash
python app.py
```

### Running in Production

For production, use a production WSGI server like Gunicorn:

```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

## Troubleshooting

### Database File Location

The SQLite database is created at: `data/todo_manager.db` (relative to where you run the app)

If you need to reset the database:
1. Stop the application
2. Delete `data/todo_manager.db`
3. Restart the application
4. The database will be recreated automatically

### Port Already in Use

If port 5000 is already in use, you can change it in `app.py`:
```python
app.run(debug=True, host='0.0.0.0', port=8080)  # Change port here
```

### Module Not Found Errors

Make sure you've installed all dependencies:
```bash
pip install -r requirements.txt
```

## Technologies Used

- **Backend**: Python Flask
- **Database**: SQLite (embedded)
- **Frontend**: HTML5, CSS3, JavaScript
- **API**: RESTful API with JSON

## Advantages of This Stack

✅ **Simple Setup** - Just install Python and run  
✅ **Fast Development** - No complex configuration  
✅ **Lightweight** - Minimal dependencies  
✅ **Perfect for Learning** - Easy to understand and modify  
✅ **Production Ready** - Can be deployed with Gunicorn/uWSGI  

## License

This project is open source and available for personal use.

