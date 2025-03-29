from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Union

router = APIRouter()
#app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


@router.get("/healthcheck", tags=["Health"])
async def healthcheck():
    """
    Health check endpoint to verify the service is running.
    """
    return {"status": "ok"}

@router.get("/items/{item_id}", tags=["Items"])
async def get_item(item_id: int):
    """
    Retrieve an item by its ID.
    """
    if item_id <= 0:
        raise HTTPException(status_code=400, detail="Invalid item ID")
    return {"item_id": item_id, "name": f"Item {item_id}"}

@router.post("/items", tags=["Items"])
async def create_item(item: dict):
    """
    Create a new item.
    """
    if "name" not in item or not item["name"]:
        raise HTTPException(status_code=400, detail="Item name is required")
    return {"message": "Item created successfully", "item": item}

@router.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@router.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}