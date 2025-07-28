from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.notification import NotificationCreate, NotificationOut
from app.schemas.user_notification import UserNotificationCreate, UserNotificationOut
from app.crud.notification import create_notification, get_notification
from app.crud.user_notification import (
    assign_notification,
    get_user_notifications,
    mark_as_read,
)
from app.database import get_db
from typing import List

router = APIRouter(prefix="/notifications", tags=["Notifications"])

@router.post("/", response_model=NotificationOut)
async def create_new_notification(data: NotificationCreate, db: AsyncSession = Depends(get_db)):
    return await create_notification(db, data)

@router.post("/assign", response_model=UserNotificationOut)
async def assign_to_user(data: UserNotificationCreate, db: AsyncSession = Depends(get_db)):
    return await assign_notification(db, data)

@router.get("/user/{user_id}", response_model=List[UserNotificationOut])
async def get_user_notifs(user_id: int, db: AsyncSession = Depends(get_db)):
    return await get_user_notifications(db, user_id)

@router.put("/read/{user_notification_id}")
async def mark_read(user_notification_id: int, db: AsyncSession = Depends(get_db)):
    return await mark_as_read(db, user_notification_id)
