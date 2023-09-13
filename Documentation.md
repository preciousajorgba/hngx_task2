
# API Documentation

This documentation provides details about the usage, endpoints, request/response formats, limitations, and deployment instructions for the FastAPI CRUD API with SQLAlchemy and SQLite.

## Table of Contents

- [API Endpoints](#api-endpoints)
- [Request and Response Formats](#request-and-response-formats)
- [Sample Usage](#sample-usage)
- [Known Limitations](#known-limitations)
- [Local Setup](#local-setup)
- [Deployment](#deployment)

## API Endpoints

The API provides the following endpoints:

1. **Create a User**
   - Endpoint: `POST /api/`
   - Description: Create a new user.
   - Request Format:
     ```json
     {
       "name": "Elon musk"
     }
     ```
   - Response Format:
     ```json
     {
       "id": 1,
       "name": "Elon musk"
     }
     ```

2. **Read All Users**
   - Endpoint: `GET /api/`
   - Description: Get a list of all users.
   - Response Format: JSON Array of Users.

3. **Read a User by ID**
   - Endpoint: `GET /api/{user_id}/`
   - Description: Get a user by their ID.
   - Response Format:
     ```json
     {
       "id": 1,
       "name": "Elon musk"
     }
     ```

4. **Update a User by ID**
   - Endpoint: `PUT /api/{user_id}/`
   - Description: Update a user's information by their ID.
   - Request Format:
     ```json
     {
       "name": "Updated Name"
     }
     ```
   - Response Format:
     ```json
     {
       "id": 1,
       "name": "Updated Name"
     }
     ```

5. **Delete a User by ID**
   - Endpoint: `DELETE /api/{user_id}/`
   - Description: Delete a user by their ID.
   - Response Format:
     ```json
     {
       "id": 1,
       "name": "Updated Name"
     }
     ```

## Request and Response Formats

- Requests should be made with a JSON payload as specified in the request format for each endpoint.
- Responses will be in JSON format as specified in the response format for each endpoint.

## Sample Usage

Here are some sample requests and responses for the API:

- **Create a User**:

  Request:
  ```json
  POST /api/
  {
    "name": "Alice Johnson"
  }
  ```

  Response:
  ```json
  {
    "id": 1,
    "name": "Alice Johnson"
  }
  ```

- **Read All Users**:

  Request:
  ```json
  GET /api/
  ```

  Response:
  ```json
  [
    {
      "id": 1,
      "name": "Elon musk"
    }
    
  ]
  ```

- **Read a User by ID**:

  Request:
  ```json
  GET /api/1/
  ```

  Response:
  ```json
  {
    "id": 1,
    "name": "Elon musk"
  }
  ```

- **Update a User by ID**:

  Request:
  ```json
  PUT /api/2/
  {
    "name": "Updated Name"
  }
  ```

  Response:
  ```json
  {
    "id": 2,
    "name": "Updated Name"
  }
  ```

- **Delete a User by ID**:

  Request:
  ```json
  DELETE /api/1/
  ```

  Response:
  ```json
  {
    "id": 1,
    "name": "Elon musk"
  }
  ```

## Known Limitations

- The API uses an SQLite database, which may not be suitable for large-scale production use. Consider using a more robust database system for production deployments.

- This is a basic CRUD API and may require additional features and security measures for real-world applications.

## Local Setup

To set up the API locally, follow these steps:

1. Clone the repository.
2. Install Python 3.x and pip if not already installed.
3. Install required dependencies using `pip install -r requirements.txt`.
4. Run the API using `uvicorn main:app --reload`.

## Deployment

For deploying the API to a server, you can follow these general steps:

1. Choose a server or cloud provider. e.g i used render
2. upload your local repo to github. It should include requirements.txt
3. integrate your github repo with render while following the instructions( this is done on render)
4. deploy by running:

    ```bash
        uvicorn main:app --reload
    ```
