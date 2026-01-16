# Employee Management REST API

## 📌 Overview

Employee Management REST API is a backend service built using **FastAPI** that provides secure and scalable APIs to manage employee records. The application supports full CRUD operations, JWT-based authentication, filtering, pagination, validation, and comprehensive unit testing.

This project follows production-grade best practices such as layered architecture, proper error handling, and isolated database testing.

---

## 🛠️ Tech Stack

* **Language**: Python 3.13
* **Framework**: FastAPI
* **ORM**: SQLAlchemy
* **Database**: SQLite (development & testing)
* **Authentication**: JWT (JSON Web Tokens)
* **Testing**: Pytest
* **API Documentation**: Swagger / OpenAPI


---

## 🚀 Running the Application Locally

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
cd app
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Swagger UI:

```
http://localhost:8000/employee/swagger/
```
---


## 📂 Project Structure

```
app/
├── main.py
├── routers/
│   ├── auth_routers.py
│   └── employee_routers.py
├── services/
│   └── employee_service.py
├── repository/
│   ├── users_repository.py
│   └── employee_repository.py
├── models/
│   ├── user.py
│   └── employee.py
├── schemas/
│   ├── auth_schemas.py
│   └── api_schemas.py
├── utils/
│   └── auth/
│       ├── jwt.py
│       └── authenticate_user.py
├── db/
│   └── database.py
└── config/
    ├── env.py
    └── constants.py

tests/
├── conftest.py
├── test_auth.py
└── test_employees.py
```

---

## 🔐 Authentication

All employee-related APIs are protected using **JWT-based authentication**.

### Register User

```
POST /auth/register
```

**Request Body**

```json
{
  "username": "admin",
  "email": "admin@example.com",
  "password": "password123"
}
```

**Response**

```
201 Created
```

---

### Login User

```
POST /auth/login
```

**Request Body**

```json
{
  "username": "admin",
  "password": "password123"
}
```

**Response**

```json
{
  "access_token": "<JWT_TOKEN>",
  "token_type": "bearer"
}
```

### Authorization Header

All secured endpoints require the following header:

```
Authorization: Bearer <JWT_TOKEN>
```

---

## 👤 Employee APIs

### Create Employee

```
POST /api/employees
```

**Request Body**

```json
{
  "name": "John Doe",
  "email": "john@example.com",
  "department": "Engineering",
  "role": "Developer"
}
```

**Responses**

* `201 Created`
* `400 Bad Request` (duplicate email)
* `401 Unauthorized`

---

### Get All Employees

```
GET /api/employees?department=Engineering&role=Developer&page=1
```

**Features**

* Pagination (10 records per page)
* Filtering by department
* Filtering by role

**Response**

```json
{
  "total": 25,
  "items": [
    {
      "id": 1,
      "name": "John Doe",
      "email": "john@example.com",
      "department": "Engineering",
      "role": "Developer",
      "date_joined": "2025-01-10"
    }
  ]
}
```

---

### Get Employee by ID

```
GET /api/employees/{id}
```

**Responses**

* `200 OK`
* `404 Not Found`
* `401 Unauthorized`

---

### Update Employee

```
PUT /api/employees/{id}
```

**Request Body**

```json
{
  "name": "John Smith",
  "department": "Sales"
}
```

**Responses**

* `200 OK`
* `404 Not Found`
* `401 Unauthorized`

---

### Delete Employee

```
DELETE /api/employees/{id}
```

**Responses**

* `204 No Content`
* `404 Not Found`
* `401 Unauthorized`

---

## ❌ Error Handling

* `400 Bad Request` → Business validation errors (duplicate email, invalid data)
* `401 Unauthorized` → Missing or invalid JWT token
* `404 Not Found` → Resource not found
* `422 Unprocessable Entity` → Request schema validation errors (FastAPI default)

---

## 🧪 Testing

Unit tests are written using **Pytest** and cover:

* Authentication (register, login, invalid credentials)
* All employee CRUD operations
* Validation errors
* Duplicate records
* Unauthorized access

### Run Tests

```bash
pytest
```

### Run Tests with Coverage

```bash
pytest --cov=app --cov-report=term-missing
```

---

## 📌 Key Highlights

* Clean layered architecture (Router → Service → Repository)
* Secure JWT-based authentication
* Proper validation and error handling
* Pagination and filtering support
* Fully isolated and reliable unit tests
* Production-ready project structure

---

## 👨‍💻 Author

Developed by **Hemanth**.
