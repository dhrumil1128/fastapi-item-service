from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field
from typing import List, Optional

# --- 4. Data Model & Schema Definition (Consolidated from schemas.py) ---

class ItemCreate(BaseModel):
    """Schema for creating a new item (Input Payload)."""
    name: str = Field(..., min_length=1)
    description: Optional[str] = None
    price: float = Field(..., gt=0, description="Price must be greater than 0")

class Item(ItemCreate):
    """Schema for returning an item (Output Payload), including its ID."""
    id: int

# --- Temporary In-Memory Database ---
# Simulates a database storage
db: dict[int, Item] = {}
next_id = 1

# --- 1. Backend Framework Initialization ---
app = FastAPI(
    title="FastAPI Item Service",
    description="A simple CRUD service implementation following the backend plan."
)

# --- 7. CORS Configuration ---
from fastapi.middleware.cors import CORSMiddleware

origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods (GET, POST, PUT, DELETE)
    allow_headers=["*"],
)

# --- 5. API Endpoint Definitions ---

# 1. POST /items/ - Create a new item.
@app.post("/items/", response_model=Item, status_code=status.HTTP_201_CREATED, summary="Create Item")
async def create_item(item_data: ItemCreate):
    global next_id
    
    # Validation for price > 0 is handled by Pydantic Field(gt=0)
    
    # FIX: Use model_dump() for modern Pydantic compatibility
    new_item = Item(id=next_id, **item_data.model_dump())
    db[next_id] = new_item
    next_id += 1
    
    return new_item

# 3. GET /items/ - Retrieve all items.
@app.get("/items/", response_model=List[Item], summary="List All Items")
async def read_items():
    return list(db.values())

# 2. GET /items/{item_id} - Retrieve a specific item by ID.
@app.get("/items/{item_id}", response_model=Item, summary="Get Item by ID")
async def read_item(item_id: int):
    # 6. Error Handling: Not Found (404)
    if item_id not in db:
        raise HTTPException(status_code=404, detail="Item not found")
    return db[item_id]

# 4. PUT /items/{item_id} - Update an existing item.
@app.put("/items/{item_id}", response_model=Item, summary="Update Item")
async def update_item(item_id: int, item_data: ItemCreate):
    # 6. Error Handling: Not Found (404)
    if item_id not in db:
        raise HTTPException(status_code=404, detail="Item not found")
        
    # Update the existing record
    # FIX: Use model_dump() for modern Pydantic compatibility
    updated_item = Item(id=item_id, **item_data.model_dump())
    db[item_id] = updated_item
    
    return updated_item

# 5. DELETE /items/{item_id} - Delete an item by ID.
@app.delete("/items/{item_id}", status_code=status.HTTP_204_NO_CONTENT, summary="Delete Item")
async def delete_item(item_id: int):
    # 6. Error Handling: Not Found (404)
    if item_id not in db:
        raise HTTPException(status_code=404, detail="Item not found")
        
    del db[item_id]
    return