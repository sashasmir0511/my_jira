from repositories.role import RoleRepository
from typing import List

from fastapi import HTTPException, status
from fastapi.params import Depends
from fastapi.routing import APIRouter
from models.role import Role
from .depends import get_role_repository

router = APIRouter()

@router.get("/", response_model=List[Role])
async def read_role(
    role: RoleRepository = Depends(get_role_repository),
    limit: int = 10,
    skip: int = 0):
    return await role.get_all(limit=limit, skip=skip)


@router.post("/", response_model=Role)
async def create_user(
    new_role: Role,
    role: RoleRepository = Depends(get_role_repository),
    ):
    return await role.create(u=new_role)
