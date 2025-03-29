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