from fastapi import FastAPI
from fastapi.security import OAuth2PasswordBearer
from fastapi.openapi.utils import get_openapi
from app.controllers.auth_controllers import auth_router
from app.controllers.app_controllers import router as app_router
from app.utils.swagger import custom_openapi, oauth2_scheme 

app = FastAPI()


# Set the custom OpenAPI schema
app.openapi = lambda: custom_openapi(app)

# Include routes from app_controllers
app.include_router(auth_router, prefix="/auth", tags=["Authentication"])
app.include_router(app_router, prefix="/api", tags=["API"])

@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI!"}