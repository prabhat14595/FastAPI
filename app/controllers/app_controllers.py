import os
from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from typing import Union
from app.db.mongodata import db
from bson import ObjectId
from app.utils.logger import logger
from app.auth_security.auth import get_current_user

router = APIRouter()

# Initialize MongoDB connection
collection_name = os.getenv("COLLECTION_NAME")
collection = db[collection_name]
logger.info(f"MongoDB collection: {collection}")

class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


router = APIRouter()


@router.get("/healthcheck", tags=["Health"])
async def healthcheck():
    """
    Health check endpoint to verify the service is running.
    """
    return {"status": "ok"}


# @router.get("/items/{item_id}", tags=["API"])
# async def get_item(item_id: int, current_user: dict = Depends(get_current_user)):
#     """
#     Retrieve an item by its ID. Requires authentication.
#     """
#     if item_id <= 0:
#         raise HTTPException(status_code=400, detail="Invalid item ID")
#     return {"item_id": item_id, "name": f"Item {item_id}", "user": current_user}


# @router.post("/items", tags=["API"])
# async def create_item(item: dict, current_user: dict = Depends(get_current_user)):
#     """
#     Create a new item. Requires authentication.
#     """
#     if "name" not in item or not item["name"]:
#         raise HTTPException(status_code=400, detail="Item name is required")
#     return {"message": "Item created successfully", "item": item, "user": current_user}


@router.post("/items/", tags=["API"])
async def create_db_item(item: dict, current_user: dict = Depends(get_current_user)):
    """
    Create a new item in the database. Requires authentication.
    """
    result = await collection.insert_one(item)
    return {"message": "Item created", "id": str(result.inserted_id), "user": current_user}


@router.get("/items/{item_id}", tags=["API"])
async def get_db_item(item_id: str, current_user: dict = Depends(get_current_user)):
    """
    Retrieve an item from the database by its ID. Requires authentication.
    """
    try:
        obj_id = ObjectId(item_id)  # Convert string ID to ObjectId
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid ID format")

    logger.info(f"Fetching item with ID: {item_id}")
    
    item = await collection.find_one({"_id": obj_id})

    if item:
        # Convert ObjectId to string
        item["_id"] = str(item["_id"])
        return {"item": item, "user": current_user}

    raise HTTPException(status_code=404, detail="Item not found")