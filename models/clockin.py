from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class ClockIn(BaseModel):
    email: EmailStr
    location: str

class UpdateClockIn(BaseModel):
    email: Optional[EmailStr] = None
    location: Optional[str] = None
