import os

# Read .env file manually and set environment variables
env_path = os.path.join(os.path.dirname(__file__), "../../.env")
with open(env_path) as f:
    for line in f:
        if line.strip() and not line.startswith("#"):  # Ignore empty lines and comments
            key, value = line.strip().split("=", 1)
            os.environ[key] = value  # Set environment variable

# Now you can access them directly
MONGO_URI = os.getenv("MONGO_URI")
DATABASE_NAME = os.getenv("DATABASE_NAME")
COLLECTION_NAME = os.getenv("COLLECTION_NAME")

#print("MONGO_URI:", MONGO_URI)  # Debugging