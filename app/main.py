from fastapi import FastAPI
# import uvicorn
# from app.controllers import app_controllers
from app.controllers.app_controllers import router as app_router

app = FastAPI()

# Include routes from app_controllers
app.include_router(app_router, prefix="/api", tags=["API"])

@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI!"}