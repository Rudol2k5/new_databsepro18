from datetime import datetime, timedelta
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.notification import Notification
from app.schemas.notification import NotificationCreate


async def create_notification(db: AsyncSession, notif: NotificationCreate):
    data = notif.model_dump()

    # Set default expires_at if not provided
    if not data.get("expires_at"):
        data["expires_at"] = datetime.utcnow() + timedelta(days=7)

    # Set default priority if not provided
    if not data.get("priority"):
        data["priority"] = 1

    new_notif = Notification(**data)
    db.add(new_notif)
    await db.commit()
    await db.refresh(new_notif)
    return new_notif


async def get_notification(db: AsyncSession, notif_id: int):
    result = await db.execute(select(Notification).where(Notification.id == notif_id))
    return result.scalar_one_or_none()


