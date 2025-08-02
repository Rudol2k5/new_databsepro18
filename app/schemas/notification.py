from datetime import datetime
from pydantic import BaseModel
from typing import Optional
from .type import NotificationTypeOut  # Assuming this is where NotificationTypeOut is imported from

class NotificationBase(BaseModel):
    title: str
    message: str
    type_id: int
    expires_at: Optional[datetime] = None
    priority: Optional[int] = 1

class NotificationCreate(NotificationBase):
    pass

class NotificationOut(NotificationBase):
    id: int
    created_at: datetime
    type: NotificationTypeOut

    class Config:
        orm_mode = True
