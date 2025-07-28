from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.notification import Notification
from app.schemas.notification import NotificationCreate


async def create_notification(db: AsyncSession, notif: NotificationCreate):
    new_notif = Notification(**notif.dict())
    db.add(new_notif)
    await db.commit()
    await db.refresh(new_notif)
    return new_notif


async def get_notification(db: AsyncSession, notif_id: int):
    result = await db.execute(select(Notification).where(Notification.id == notif_id))
    return result.scalar_one_or_none()

