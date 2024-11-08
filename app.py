from fastapi import FastAPI
from typing import Union
from pydantic import BaseModel

app = FastAPI()


@app.get("/items/{item_id}")
def get_item_by_id(item_id:int):
    return {"message":f"we know that you request item id : {item_id}"}

@app.get("/items")
def search_items(search_key:Union[str,None]=None):
    return {"message":f"you are search and item start by {search_key}"}

class Item(BaseModel):
    name: str
    price : float

@app.post("/items")
def create_new_item(item:Item):
    # create item 
    return {"message":f"item name is {item.name}"}
    
@app.put("/items/{item_id}")
def update_item(item_id:int,item:Item):
    #update item
    return {"message":f"item updated is {item.name} {item.price}"}

@app.delete("/items/{item_id}")
def delete_item(item_id:int):
    #delete item 
    return {"message":f"item deleted is {item_id}"}