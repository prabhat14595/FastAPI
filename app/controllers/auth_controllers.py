import os
from dotenv import load_dotenv
from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from typing import Dict
from app.db.mongodata import db
from app.utils.logger import logger
from fastapi.security import OAuth2PasswordRequestForm
from app.auth_security.auth import authenticate_user, create_access_token, get_current_user
from typing import Dict
from pydantic import BaseModel
import hashlib
load_dotenv()

auth_router = APIRouter()

# Initialize MongoDB connection
collection_name = os.getenv("COLLECTION_NAME_AUTH")
users_collection = db[collection_name]
logger.info(f"MongoDB Auth collection: {users_collection}")


# In-memory user store for simplicity (replace with a database in production)
users_db: Dict[str, dict] = {}


# Define a simple user registration model
class UserRegister(BaseModel):
    username: str
    password: str


@auth_router.post("/register", tags=["Authentication"])
async def register(user: UserRegister):
    # Check if the username already exists in MongoDB
    logger.info(f"Registering user: {user.username}")
    logger.info(f"MongoDB Auth collection: {users_collection}")
    
    # Use `await` for the asynchronous `find_one` query
    existing_user = await users_collection.find_one({"username": user.username})
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already registered",
        )
    
    # Hash the password before saving it
    hashed_password = hashlib.sha256(user.password.encode()).hexdigest()
    
    # Save the user to MongoDB
    await users_collection.insert_one({"username": user.username, "password": hashed_password})
    return {"message": "User registered successfully Welcome"}


@auth_router.post("/token", tags=["Authentication"])
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    # Find the user in MongoDB
    user = await users_collection.find_one({"username": form_data.username})
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    # Verify the password
    hashed_password = hashlib.sha256(form_data.password.encode()).hexdigest()
    if user["password"] != hashed_password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    # Generate access token
    access_token = create_access_token(data={"sub": user["username"]})
    return {"access_token": access_token, "token_type": "bearer"}