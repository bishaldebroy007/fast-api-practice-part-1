# FastAPI CRUD API - Learning Project
A simple FastAPI application demonstrating basic CRUD (Create, Read, Update, Delete) operations with an in-memory data store.
## Environment Setup

To create a virtual environment(linux):
```bash
python3 -m venv venv
```

To activate that:

```bash
source venv/bin/activate
```

Optional (this is kind of package.json in javascript projects)

```bash
pip freeze > requirements.txt
```



## Code Overview
This is a basic REST API built with FastAPI that manages a collection of items with `id`, `name`, and `origin` properties.

## Dependencies

```python
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
```

- FastAPI: The web framework for building APIs.
- Pydantic: Data validation using Python type annotations.
- typing.List: Type hints for lists

## Data Model

```python
class Home_Class(BaseModel):
    id: int
    name: str
    origin: str
```
The `Home_Class` uses Pydantic's `BaseModel` for automatic validation and serialization of incoming/outgoing data.

## In-Memory Storage

```python
data: List[Home_Class] = []
```
Data is stored in memory (will reset when the server restarts).

## API Endpoints

### 1. Root Endpoint

- Method: GET
- Path: /
- Purpose: Welcome message
- Response: {"message": "Welcome to the API!"}

### 2. Get All Items

- Method: GET
- Path: /about
- Purpose: Retrieve all items from the data store
- Response: List of all items

### 3. Create New Item

- Method: POST
- Path: /about
- Purpose: Add a new item to the data store
- Request Body:

```python
  {
    "id": 1,
    "name": "Example",
    "origin": "Location"
  }
```
- Response: The created item
- Note: There's a bug in the original code - it should be data.append(tea) not data.append(data)

### 4. Update Item

- Method: PUT
- Path: /about/{home_id}
- Purpose: Update an existing item by ID
- Path Parameter: home_id (int)
- Request Body: Updated item data
- Response: Updated item or error message

### Delete Item

- Method: DELETE
- Path: /about/{home_id}
- Purpose: Delete an item by ID
- Path Parameter: home_id (int)
- Response: Success message or error message.

## Running the Application

```python
# Install FastAPI and uvicorn
pip install fastapi uvicorn

# Run the server
uvicorn filename:app --reload
```

Replace `filename` with your Python file name (without .py extension).


## Testing the API

Once running, you can access:

- Interactive API docs: http://127.0.0.1:8000/docs (Swagger UI)
- Alternative docs: http://127.0.0.1:8000/redoc (ReDoc)

## Important Notes

- Bug in POST endpoint: The line `data.append(data)` should be `data.append(data)` to correctly add the new item.
- Data Persistence: Data is stored in memory only. It will be lost when the server restarts. For persistence, you'd need to use a database.

## Key Learning Points

1. FastAPI decorators (`@app.get()`, `@app.post()`, etc.) define routes
2. Pydantic models automatically validate request/response data
3. Path parameters are defined in the route path (e.g., `{home_id}`)
4. Type hints make the code more readable and enable automatic validation
5. In-memory storage is simple but not production-ready

## Next Steps for Learning

- Add query parameters for filtering
- Implement proper error handling with HTTP status codes
- Connect to a database (SQLAlchemy)
- Add authentication and authorization
- Learn about FastAPI's dependency injection system
- Explore async/await for database operations

# Reference

- [YouTube](https://youtu.be/foGklduxhM0?si=QIsip5EKq8IeODVJ)