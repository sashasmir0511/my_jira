from .base import BaseRepository
from typing import List, Optional
from models.role import Role
from db.role import role


class RoleRepository(BaseRepository):
    
    async def get_all(self, limit: int = 10, skip: int = 0) -> List[Role]:
        query = role.select().limit(limit).offset(skip)
        return await self.database.fetch_all(query=query)

    
    async def get_by_id(self, id: int) -> Optional[Role]:
        query = role.select().where(role.c.id==id)
        role_by_id = await self.database.fetch_one(query=query)
        if role_by_id is None:
            return None
        return Role.parse_obj(role_by_id)

    
    async def create(self, u: Role) -> Role:
        values = {"name": u.name}
        query = role.insert().values(**values)
        role.id = await self.database.execute(query=query)
        return u

    
    async def update(self, id: int, u: Role) -> Role:
        values = {"name": u.name}
        query = role.update().where(role.c.id==id).values(**values)
        await self.database.execute(query=query)
        return u