from datetime import datetime
from pydantic import BaseModel
from app.schemas.type import NotificationTypeOut


class NotificationBase(BaseModel):
    title: str
    message: str
    type_id: int


class NotificationCreate(NotificationBase):
    pass


class NotificationOut(NotificationBase):
    id: int
    created_at: datetime
    type: NotificationTypeOut

    class Config:
        orm_mode = True

