# FastAPI Item Service Backend

This repository hosts the backend application built using FastAPI for managing simple items. It implements full CRUD operations with Pydantic validation and CORS configuration for local development.

## Project Structure
- `main.py`: Contains the FastAPI application, models, and endpoints.
- `requirements.txt`: Lists all necessary Python dependencies.

## Setup Instructions (Local Development)
1. **Clone the repository:**
   ```bash
   git clone https://github.com/your_username/fastapi-item-service
   cd fastapi-item-service
   ```
2. **Create and activate a virtual environment (recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Linux/macOS
   .\venv\Scripts\activate   # On Windows
   ```
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Run the server using Uvicorn:**
   ```bash
   uvicorn main:app --reload --host 0.0.0.0 --port 8000
   ```
5. **Access Documentation:**
   The interactive API documentation will be available at: `http://127.0.0.1:8000/docs`

## API Endpoints Overview
The service exposes the following endpoints for Item management:
- `POST /items/`: Create a new item.
- `GET /items/`: List all items.
- `GET /items/{item_id}`: Retrieve an item by ID.
- `PUT /items/{item_id}`: Update an existing item.
- `DELETE /items/{item_id}`: Delete an item by ID.