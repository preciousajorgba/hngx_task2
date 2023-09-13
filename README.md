


# FastAPI CRUD API with SQLAlchemy and SQLite

This FastAPI CRUD API provides endpoints to perform CRUD (Create, Read, Update, Delete) operations on user records using SQLAlchemy and SQLite as the database.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
- [API Endpoints](#api-endpoints)
  - [Create a User](#create-a-user)
  - [Read All Users](#read-all-users)
  - [Read a User by ID](#read-a-user-by-id)
  - [Update a User by ID](#update-a-user-by-id)
  - [Delete a User by ID](#delete-a-user-by-id)
- [Running the API](#running-the-api)
- [Sample Requests](#sample-requests)
- [Known Limitations](#known-limitations)

## Prerequisites

Before you can set up, run, and use the API, make sure you have the following prerequisites installed:

- Python 3.x
- pip (Python package manager)

## Getting Started

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

## API Endpoints

### Create a User

- **URL**: `/api/`
- **Method**: `POST`
- **Request Body**: JSON
  ```json
  {
    "name": "mark essien"
  }
  ```
- **Response**: JSON
  ```json
  {
    "id": 1,
    "name": "mark essien"
  }
  ```

### Read All Users

- **URL**: `/api/`
- **Method**: `GET`
- **Query Parameters**:
  - `skip` (optional): Number of records to skip (default: 0)
  - `limit` (optional): Maximum number of records to return (default: 100)
- **Response**: JSON Array of Users

### Read a User by ID

- **URL**: `/api/{user_id}/`
- **Method**: `GET`
- **Response**: JSON
  ```json
  {
    "id": 1,
    "name": "mark essien"
  }
  ```

### Update a User by ID

- **URL**: `/api/{user_id}/`
- **Method**: `PUT`
- **Request Body**: JSON
  ```json
  {
    "name": "Updated Name"
  }
  ```
- **Response**: JSON
  ```json
  {
    "id": 1,
    "name": "Updated Name"
  }
  ```

### Delete a User by ID

- **URL**: `/api/{user_id}/`
- **Method**: `DELETE`
- **Response**: JSON
  ```json
  {
    "id": 1,
    "name": "Updated Name"
  }
  ```

## Running the API

To run the API, execute the following command in the project directory:

```bash
uvicorn main:app --reload
```

The API will be available at `http://127.0.0.1:8000/`. You can access the Swagger documentation at `http://127.0.0.1:8000/docs` and the ReDoc documentation at `http://127.0.0.1:8000/redoc`.

## Sample Requests

Here are some sample requests you can make to the API:

- for local server, replace "https://hngx-task2-qh6l.onrender.com" with "http://127.0.0.1:8000"

- Create a User:
  ```bash
  curl -X POST -H "Content-Type: application/json" -d '{"name": "mark essien"}' https://hngx-task2-qh6l.onrender.com/api/
  ```

- Read All Users:
  ```bash
  curl https://hngx-task2-qh6l.onrender.com/api/
  ```

- Read a User by ID:
  ```bash
  curl https://hngx-task2-qh6l.onrender.com/api/1/
  ```

- Update a User by ID:
  ```bash
  curl -X PUT -H "Content-Type: application/json" -d '{"name": "Updated Name"}' https://hngx-task2-qh6l.onrender.com/api/1/
  ```

- Delete a User by ID:
  ```bash
  curl -X DELETE https://hngx-task2-qh6l.onrender.com/api/1/
  ```

## Known Limitations

- This API uses an SQLite database, which may not be suitable for large-scale production use. Consider using a more robust database system for production deployments.
- This is a basic CRUD API and may require additional features and security measures for real-world applications.
```

