# Expense Tracker

A full-stack expense tracking application built with FastAPI, React, and MySQL.

## Features

- User authentication (register/login)
- JWT token-based authentication
- CRUD operations for expenses
- Category management
- Responsive UI
- Secure password hashing
- Database relationships

## Tech Stack

### Backend
- FastAPI (Python web framework)
- SQLAlchemy (ORM)
- MySQL (Database)
- JWT (Authentication)
- Python-dotenv (Environment variables)

### Frontend
- React
- JavaScript
- CSS
- Axios (HTTP client)

## Prerequisites

- Python 3.8+
- Node.js and npm
- MySQL Server

## Setup Instructions

1. Clone the repository:
```bash
git clone <repository-url>
cd Expense-Tracker
```

2. Set up the backend:
```bash
cd backend
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

3. Create a `.env` file in the backend directory:
```
MYSQL_USER=your_mysql_username
MYSQL_PASSWORD=your_mysql_password
MYSQL_HOST=localhost
MYSQL_PORT=3306
MYSQL_DATABASE=expense_tracker
SECRET_KEY=your-secret-key-here
```

4. Create the MySQL database:
```sql
CREATE DATABASE expense_tracker;
```

5. Initialize the database tables:
```bash
python init_db.py
```

6. Start the backend server:
```bash
uvicorn main:app --reload
```

7. Set up the frontend:
```bash
cd frontend
npm install
```

8. Create a `.env` file in the frontend directory:
```
REACT_APP_API_URL=http://localhost:8000
```

9. Start the frontend development server:
```bash
npm start
```

## API Endpoints

### Authentication
- POST /api/auth/register - Register a new user
- POST /api/auth/login - Login user

### Expenses
- GET /api/expenses - Get all expenses
- POST /api/expenses - Create a new expense
- GET /api/expenses/{id} - Get a specific expense
- PUT /api/expenses/{id} - Update an expense
- DELETE /api/expenses/{id} - Delete an expense

### Categories
- GET /api/categories - Get all categories
- POST /api/categories - Create a new category
- GET /api/categories/{id} - Get a specific category
- PUT /api/categories/{id} - Update a category
- DELETE /api/categories/{id} - Delete a category

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

