from fastapi import FastAPI  # Importing FastAPI framework to create the web API
from pydantic import BaseModel  # Importing BaseModel from Pydantic to define data models
from typing import List  # Importing List for handling multiple items

# Define a data model using Pydantic
class Item(BaseModel):
    name: str  # Name of the item (string type)
    description: str  # Description of the item (string type)
    price: float  # Price of the item (float type)

# Create an instance of FastAPI
app = FastAPI()

# Define a route for the home page
@app.get("/")  # This means when a GET request is made to the root URL ("/")
def home():
    return {"message": "Hello World"}  # Return a simple JSON response

# Define a route to read an item with an optional query parameter
@app.get("/items/{item_id}")  # This means when a GET request is made to "/items/{item_id}"
def read_item(item_id: int, q: str = None):  # item_id is a required integer, q is an optional string
    return {"item_id": item_id, "q": q}  # Return the item ID and query string in a JSON response

# Define a route to create a new item
@app.post("/items")  # This means when a POST request is made to "/items"
def create_item(item: Item):  # Accepts JSON data based on the Item model
    return {
        "message": "Item has been created",  # Success message
        "item_name": item.name,  # Returning the name of the created item
        "item_price": item.price,  # Returning the price of the created item
        "item_description": item.description,  # Returning the description of the created item
    }

# Define a route to update an existing item
@app.put("/items/{item_id}")  # This means when a PUT request is made to "/items/{item_id}"
def update_item(item_id: int, item: Item):  # Accepts item ID and new item details
    return {
        "message": "Item has been updated",  # Success message
        "item_id": item_id,  # Returning the item ID
        "updated_name": item.name,  # Returning updated name
        "updated_price": item.price,  # Returning updated price
        "updated_description": item.description,  # Returning updated description
    }

# Define a route to delete an item
@app.delete("/items/{item_id}")  # This means when a DELETE request is made to "/items/{item_id}"
def delete_item(item_id: int):  # Accepts item ID to delete
    return {"message": f"Item with ID {item_id} has been deleted"}  # Return deletion confirmation

# Define a route to get multiple items
@app.get("/items")  # This means when a GET request is made to "/items"
def get_all_items():
    sample_items = [
        {"name": "Laptop", "description": "Gaming laptop", "price": 1200.99},
        {"name": "Smartphone", "description": "Android smartphone", "price": 699.99},
        {"name": "Headphones", "description": "Noise-canceling headphones", "price": 199.99},
    ]  # Sample data to return multiple items
    return {"items": sample_items}  # Return the list of items
