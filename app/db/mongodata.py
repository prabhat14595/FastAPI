import os
from dotenv import load_dotenv
from motor.motor_asyncio import AsyncIOMotorClient

# Explicitly load .env
load_dotenv()

# Read environment variables
MONGO_URI = os.getenv("MONGO_URI")
DATABASE_NAME = os.getenv("DATABASE_NAME")

#print("MONGO_URI (after dotenv):", MONGO_URI)

if not MONGO_URI:
    raise ValueError("❌ ERROR: MONGO_URI is not set! Ensure `.env` exists.")

# Initialize MongoDB connection
client = AsyncIOMotorClient(MONGO_URI)
db = client[DATABASE_NAME]