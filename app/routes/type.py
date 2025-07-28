from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.type import NotificationTypeCreate, NotificationTypeOut
from app.crud.type import create_type, get_all_types
from app.database import get_db
from typing import List

router = APIRouter(prefix="/types", tags=["Notification Types"])

@router.post("/", response_model=NotificationTypeOut)
async def create_notification_type(type_data: NotificationTypeCreate, db: AsyncSession = Depends(get_db)):
    return await create_type(db, type_data)

@router.get("/", response_model=List[NotificationTypeOut])
async def list_notification_types(db: AsyncSession = Depends(get_db)):
    return await get_all_types(db)
