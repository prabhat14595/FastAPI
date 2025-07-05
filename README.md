### Setup Instructions

1. Install Python 3.11 and set it as the default version:
    ```bash
    brew install python@3.11 && brew unlink python@3.9 && brew link python@3.11
    python --version
    ```

2. Verify Python installation:
    ```bash
    python --version
    python3 --version
    ```

3. Set Python 3 as the default `python` command:
    ```bash
    alias python='python3'
    python --version
    ```

4. Install additional Python dependencies:
    ```bash
    brew install python-gdbm@3.11
    ```

5. Create a virtual environment:
    ```bash
    python -m venv .venv
    ```

6. Set up the project directory structure:
    ```bash
    mkdir -p project/app/{models,views,controllers,db,schemas,utils,tests} project/alembic/versions
    ```

7. Create necessary files:
    ```bash
    touch project/app/{__init__.py,main.py} \
            project/app/models/__init__.py \
            project/app/views/__init__.py \
            project/app/controllers/__init__.py \
            project/app/db/__init__.py \
            project/app/schemas/__init__.py \
            project/app/utils/__init__.py \
            project/app/tests/__init__.py \
            project/.env \
            project/requirements.txt \
            project/README.md \
            project/alembic/env.py \
            project/alembic/README
    ```

    Ensure that `project/app/main.py` contains an ASGI app named `app`, for example:
    ```python
    from fastapi import FastAPI

    app = FastAPI()

    @app.get("/")
    def read_root():
        return {"message": "Hello, World!"}
    ```


## Run these commands to run the application
    ```bash
    # Upgrade pip to the latest version
    python3 -m pip install --upgrade pip

    # Install project dependencies
    python -m pip install -r requirements.txt

    # Set the PYTHONPATH environment variable and run the application
    fastapi dev main.py
    ```


## Set .env file here which contains the below configs for application to run 
```bash
MONGO_URI=mongodb://localhost:27017
DATABASE_NAME=<DB_name>
COLLECTION_NAME=workspace
COLLECTION_NAME_AUTH=users
LOG_PATH=/path/to/logs
SECRET_KEY='Your Secret Key'
ALGORITHM=HS256
# Duration (in minutes) for which the access token remains valid (default: 30 minutes)
ACCESS_TOKEN_EXPIRE_MINUTES=30
```


##Docker Image running 
```bash
    docker build -t your-docker-registry/fastapi-app:latestV0.0.2 .  
    docker run -p 8000:8000 your-docker-registry/fastapi-app:latestV0.0.2
    ## Env file 
    docker run --env-file .env -p 8000:8000 your-docker-registry/fastapi-app:latestV0.0.2
```


## Frontend (React) Usage

The `frontend/` folder contains a React app that provides a UI for all FastAPI endpoints.

### Features
- User Registration (`/auth/register`)
- User Login (`/auth/token`)
- Access Protected Endpoint (`/auth/protected`)
- Healthcheck (`/api/healthcheck`)
- Create Item (`/api/items/`)
- Get Item by ID (`/api/items/{item_id}`)

### How to Run the Frontend

1. Go to the frontend directory:
    ```bash
    cd frontend
    ```
2. Install dependencies:
    ```bash
    npm install
    ```
3. Start the React app:
    ```bash
    npm start
    ```
4. The app will be available at [http://localhost:3000](http://localhost:3000)

### Project Structure (Frontend)
- `src/api.js` — API utility for all backend endpoints
- `src/Register.js` — User registration form
- `src/Login.js` — User login form
- `src/Protected.js` — Protected endpoint access
- `src/Healthcheck.js` — Health check UI
- `src/CreateItem.js` — Create item form
- `src/GetItem.js` — Get item by ID form
- `src/App.js` — Main app, renders all components

### Authentication
- JWT token is stored in `localStorage` after login.
- All protected endpoints require the token in the `Authorization: Bearer <token>` header.

---


