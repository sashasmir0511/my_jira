from typing import Optional
from pydantic import BaseModel, validator, constr, EmailStr


class User(BaseModel):
    id: Optional[int] = None
    email: EmailStr
    name: str
    hashed_password: str
    is_active: bool


class UserIn(BaseModel):
    email: EmailStr
    name: str
    password: constr(min_length=4)
    password2: str
    is_active: bool = False

    @validator("password2")
    def password_match(cls, v, values):
        if 'password' in values \
            and v != values["password"]:
            raise ValueError("password don't match")
        return v