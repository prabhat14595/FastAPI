from fastapi import FastAPI
from fastapi.security import OAuth2PasswordBearer
from fastapi.openapi.utils import get_openapi
from app.controllers.auth_controllers import auth_router
from app.controllers.app_controllers import router as app_router

app = FastAPI()

# Define OAuth2 security scheme for Swagger
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/token")

# Custom OpenAPI schema to include security definitions
def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="FastAPI Application",
        version="1.0.0",
        description="This is a sample FastAPI application with authentication.",
        routes=app.routes,
    )
    openapi_schema["components"]["securitySchemes"] = {
        "OAuth2PasswordBearer": {
            "type": "oauth2",
            "flows": {
                "password": {
                    "tokenUrl": "/auth/token",
                    "scopes": {}
                }
            }
        }
    }
    for path in openapi_schema["paths"].values():
        for method in path.values():
            method["security"] = [{"OAuth2PasswordBearer": []}]
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi

# Include routes from app_controllers
app.include_router(auth_router, prefix="/auth", tags=["Authentication"])
app.include_router(app_router, prefix="/api", tags=["API"])

@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI!"}