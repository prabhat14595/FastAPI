from pydantic_settings import BaseSettings
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Settings(BaseSettings):
    MONGO_URI: str
    DATABASE_NAME: str
    COLLECTION_NAME: str

    class Config:
        env_file = ".env"  # Points to your .env file

# Create an instance of Settings
settings = Settings()