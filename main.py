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
<<<<<<< HEAD
    return items
=======
    return items
>>>>>>> c66d0c55605053b9327547392d7029bb0e145e45
