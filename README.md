# FastAPI Setup Guide

## 1. Initialize the Project with `uv`

Before starting, initialize the project using `uv`:

```sh
uv init
```

## 2. Create and Activate a Virtual Environment

After initializing, activate the virtual environment:

- On Windows (PowerShell):
  ```sh
  .venv\Scripts\activate
  ```
- On macOS/Linux:
  ```sh
  source .venv/bin/activate
  ```

## 3. Install FastAPI and Uvicorn

Use `uv` to install the required packages:

```sh
uv add fastapi uvicorn
```

## 4. Create the `main.py` File

Now, create a file named `main.py` and add the following code:

### Basic FastAPI Setup

```python
from fastapi import FastAPI  # Importing FastAPI framework to create the web API

app = FastAPI()

@app.get("/")  # Root endpoint
def home():
    return {"message": "Hello World"}  # Return a simple JSON response
```

#### Explanation:
- **FastAPI Instance:** `app = FastAPI()` creates the application.
- **Root Route (`/`)**: Returns a simple JSON message "Hello World".

### Read Item Endpoint

```python
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
```

#### Explanation:
- **Dynamic Route (`/items/{item_id}`)**: Accepts an integer `item_id` and an optional query parameter `q`.
- **Returns:** A JSON response containing `item_id` and optional `q`.

### Create Item Endpoint (POST Request)

```python
from pydantic import BaseModel  # Importing BaseModel from Pydantic to define data models

class Item(BaseModel):
    name: str  # Name of the item (string type)
    description: str  # Description of the item (string type)
    price: float  # Price of the item (float type)

@app.post("/items")
def create_item(item: Item):
    return {
        "message": "Item has been created",
        "item_name": item.name,
        "item_price": item.price,
        "item_description": item.description,
    }
```

#### Explanation:
- **Pydantic Model (`Item`)**: Defines a structure with `name`, `description`, and `price`.
- **POST Request (`/items`)**: Accepts a JSON request body matching the `Item` model and returns a confirmation message.

### Update Item Endpoint (PUT Request)

```python
@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {
        "message": "Item has been updated",
        "item_id": item_id,
        "updated_name": item.name,
        "updated_price": item.price,
        "updated_description": item.description,
    }
```

#### Explanation:
- **PUT Request (`/items/{item_id}`)**: Updates an existing item by its `item_id`.
- **Returns**: Updated item details.

### Delete Item Endpoint

```python
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    return {"message": f"Item with ID {item_id} has been deleted"}
```

#### Explanation:
- **DELETE Request (`/items/{item_id}`)**: Deletes an item using its `item_id`.
- **Returns**: Confirmation message.

### Retrieve All Items Endpoint

```python
@app.get("/items")
def get_all_items():
    sample_items = [
        {"name": "Laptop", "description": "Gaming laptop", "price": 1200.99},
        {"name": "Smartphone", "description": "Android smartphone", "price": 699.99},
        {"name": "Headphones", "description": "Noise-canceling headphones", "price": 199.99},
    ]
    return {"items": sample_items}
```

#### Explanation:
- **GET Request (`/items`)**: Returns a list of sample items.
- **Static Data**: Used as an example for multiple items.

## 5. Run the FastAPI Server

To run the server, use Uvicorn:

```sh
uvicorn main:app --reload
```

- `main:app` → `main.py` file and `app` FastAPI instance.
- `--reload` → Enables auto-reloading when changes are made.

After running the command, you should see an output like this:

```
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
```

## 6. Test Your API

Open your browser and visit:

- `http://127.0.0.1:8000/` → Should return `{"message": "Hello World"}`.
- `http://127.0.0.1:8000/items/1?q=example` → Should return `{"item_id": 1, "q": "example"}`.

## 7. Interactive API Docs

FastAPI provides automatic documentation:

- Open `http://127.0.0.1:8000/docs` → Swagger UI.
- Open `http://127.0.0.1:8000/redoc` → ReDoc UI.

These allow you to test your endpoints directly from the browser!

---

This is your basic FastAPI setup guide! Now you can extend it with more routes, validations, and features. 🚀

