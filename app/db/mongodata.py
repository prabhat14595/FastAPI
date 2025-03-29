from motor.motor_asyncio import AsyncIOMotorClient
from app.config.settings import settings  # Import the settings class

# Initialize MongoDB connection
client = AsyncIOMotorClient(settings.MONGO_URI)
db = client[settings.DATABASE_NAME]