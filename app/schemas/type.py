from pydantic import BaseModel


class NotificationTypeBase(BaseModel):
    type_name: str
    description: str = None


class NotificationTypeCreate(NotificationTypeBase):
    pass


class NotificationTypeOut(NotificationTypeBase):
    id: int

    class Config:
        orm_mode = True

