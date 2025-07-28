from datetime import datetime
from pydantic import BaseModel
from app.schemas.notification import NotificationOut


class UserNotificationBase(BaseModel):
    user_id: int
    notification_id: int


class UserNotificationCreate(UserNotificationBase):
    pass


class UserNotificationOut(BaseModel):
    id: int
    is_read: bool
    read_at: datetime | None
    notification: NotificationOut

    class Config:
        orm_mode = True

