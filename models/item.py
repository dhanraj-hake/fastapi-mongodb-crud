from pydantic import BaseModel, EmailStr
from datetime import date
from typing import Optional

class Item(BaseModel):
    name : str
    email : EmailStr
    item_name : str
    quantity : float
    expiry_date : date

class UpdateItem(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    item_name: Optional[str] = None
    quantity: Optional[int] = None
    expiry_date: Optional[date] = None