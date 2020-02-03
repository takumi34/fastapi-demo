from fastapi import FastAPI
from pydantic import BaseModel
from enum import Enum
app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/chika")
def read_chika():
    return {"Chika"}


@app.get("/items/{item_id}")
def read_item(item_id):
    return {"item_id": item_id}


@app.get("/item/{id}")
def read_item2(id: int):
    return {"id": id}


class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = None


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}


@app.get("/users/chika")
async def read_user_chika():
    return {"user_id": "I'm chika!"}


@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}


class AlphaName(str, Enum):
    aiu = "aiu"
    uia = "uia"


@app.get("/alpha/{alpha_name}")
async def get_model(alpha_name: AlphaName):
    if alpha_name == AlphaName.aiu:
        return {"name": alpha_name}
    return {"name": AlphaName.uia}