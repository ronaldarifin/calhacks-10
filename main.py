from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}

items = [
    {"item_id": 1, "name": "Item 1"},
    {"item_id": 2, "name": "Item 2"},
]

# Define a GET endpoint to retrieve all items
@app.get("/items")
def get_items():
    return items
