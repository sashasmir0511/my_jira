from typing import Optional
from pydantic import BaseModel, validator, constr, EmailStr

class Role(BaseModel):
    id: Optional[int] = None
    name: str
