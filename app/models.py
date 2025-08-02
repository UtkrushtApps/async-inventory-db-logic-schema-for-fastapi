from sqlalchemy.orm import declarative_base
from pydantic import BaseModel, Field
from typing import Optional
from decimal import Decimal
from datetime import datetime

Base = declarative_base()
# Implement SQLAlchemy model for 'products' table and Pydantic schemas for request/response below

class ProductCreate(BaseModel):
    # Define product creation schema (fields: name, sku, quantity, price)
    pass

class ProductOut(BaseModel):
    # Define product response schema (fields: id, name, sku, quantity, price, created_at)
    pass

# Define Product DB model here (to match schema.sql)
