# Employee Management REST API (Flask)

This project is a basic REST API built using Flask to manage employees in a company.
It focuses on CRUD operations, RESTful principles, JWT authentication, filtering,
pagination, and automated testing using pytest.

--------------------------------------------------

TECH STACK

Python 3  
Flask  
Flask-SQLAlchemy  
PyJWT  
SQLite  
Pytest  



INSTALLATION

1. Clone the repository

git clone https://github.com/kumarpradeep78/python_flask_backend_API.git
cd python_flask_backend_API

2. Install dependencies

pip install -r requirements.txt

3. Run the application

python app.py

The server will start at:

http://127.0.0.1:8000

--------------------------------------------------

AUTHENTICATION (JWT)

All employee APIs are protected.
You must generate a token before performing any CRUD operation.

Generate Token

Send a GET request:

http://127.0.0.1:8000/login

Response example:

{
  "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}

Copy this token and use it in the Authorization header.

--------------------------------------------------

USING TOKEN IN POSTMAN

Header Key:
Authorization

Header Value:
Bearer <your_token_here>

--------------------------------------------------

EMPLOYEE API ENDPOINTS

Create Employee  
POST http://127.0.0.1:8000/api/employees

Body (JSON):

{
  "name": "Bob",
  "email": "bob@example.com",
  "department": "Engineering",
  "role": "Developer"
}

--------------------------------------------------

Get All Employees  
GET http://127.0.0.1:8000/api/employees

