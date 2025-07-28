from sqlalchemy import Column, Integer, String
from app.database import Base

class NotificationType(Base):
    __tablename__ = "notification_types"

    id = Column(Integer, primary_key=True, index=True)
    type_name = Column(String, unique=True, nullable=False)
    description = Column(String)

