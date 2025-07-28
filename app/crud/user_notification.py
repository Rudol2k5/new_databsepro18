from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import update
from datetime import datetime
from app.models.user_notification import UserNotification
from app.schemas.user_notification import UserNotificationCreate


async def assign_notification(db: AsyncSession, notif_data: UserNotificationCreate):
    new_user_notif = UserNotification(**notif_data.dict())
    db.add(new_user_notif)
    await db.commit()
    await db.refresh(new_user_notif)
    return new_user_notif


async def get_user_notifications(db: AsyncSession, user_id: int):
    result = await db.execute(
        select(UserNotification).where(UserNotification.user_id == user_id)
    )
    return result.scalars().all()


async def mark_as_read(db: AsyncSession, user_notif_id: int):
    stmt = (
        update(UserNotification)
        .where(UserNotification.id == user_notif_id)
        .values(is_read=True, read_at=datetime.utcnow())
        .execution_options(synchronize_session="fetch")
    )
    await db.execute(stmt)
    await db.commit()
    return {"message": "Notification marked as read."}
