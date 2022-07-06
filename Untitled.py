from typing import Optional
from fastapi import FastAPI,Path,HTTPException
from pydantic import BaseModel
from typing import Optional
class Item(BaseModel):
    id: int
    name: str
    price: int
    brand: Optional[str] = None
inventory = {}

app = FastAPI()
@app.get("/")
def firstPage():
    return {"test" : True}
@app.get("/home")
def home():
    return {"test" : "notAccesable" }

@app.get("/get-item/{item_id}")
def showItem(item_id : int = Path(None,description = "Please enter the id of item that you want to see from inventory ",gt=0)):
    if item_id in inventory:
        return inventory[item_id]
    return {"error" : "Your item does not exist."}




@app.post("/add-items/{item_id}")
def add_items(Item : Item,item_id : int):
    if item_id in inventory:
        return {"error" : "The item does already exists"}
    inventory[item_id] = Item
    return inventory[item_id]

   