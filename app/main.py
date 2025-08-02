from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db
from app import models
from typing import List

app = FastAPI(title="Inventory Management API")

@app.post("/products", response_model=models.ProductOut)
async def add_product(product: models.ProductCreate, db: AsyncSession = Depends(get_db)):
    # Accepts product data and adds to DB (logic to be implemented in models.py)
    pass

@app.get("/products", response_model=List[models.ProductOut])
async def list_products(db: AsyncSession = Depends(get_db)):
    # Fetches all products from DB (logic to be implemented in models.py)
    pass
