from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.type import NotificationType
from app.schemas.type import NotificationTypeCreate


async def create_type(db: AsyncSession, notif_type: NotificationTypeCreate):
    new_type = NotificationType(**notif_type.dict())
    db.add(new_type)
    await db.commit()
    await db.refresh(new_type)
    return new_type


async def get_all_types(db: AsyncSession):
    result = await db.execute(select(NotificationType))
    return result.scalars().all()

