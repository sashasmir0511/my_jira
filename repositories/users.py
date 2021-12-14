from db.users import users
from .base import BaseRepository
from core.security import hash_password
from typing import List, Optional
from models.user import User, UserIn

class UserRepository(BaseRepository):


    async def get_all(self, limit: int = 10, skip: int = 0) -> List[User]:
        query = users.select().limit(limit).offset(skip)
        return await self.database.fetch_all(query=query)


    async def get_by_id(self, id: int) -> Optional[User]:
        query = users.select().where(users.c.id==id)
        user_by_id = await self.database.fetch_one(query=query)
        if user_by_id is None:
            return None
        return User.parse_obj(user_by_id)


    async def get_by_email(self, email: str) -> Optional[User]:
        query = users.select().where(users.c.email==email)
        user_by_email = await self.database.fetch_one(query=query)
        if user_by_email is None:
            return None
        return User.parse_obj(user_by_email)


    async def create(self, u: UserIn) -> User:
        user = User(
            name = u.name,
            email = u.email,
            hashed_password = hash_password(u.password),
            is_active = u.is_active,
        )
        values = {**user.dict()}
        values.pop("id", None)
        query = users.insert().values(**values)
        user.id = await self.database.execute(query=query)
        return user


    async def update(self, id: int, u: UserIn) -> User:
        user = User(
            id = id,
            email = u.email,
            name = u.name,
            hashed_password = hash_password(u.password),
            is_active = u.is_active,
        )
        values = {**user.dict()}
        values.pop("id", None)
        query = users.update().where(users.c.id==id).values(**values)
        await self.database.execute(query=query)
        return user

