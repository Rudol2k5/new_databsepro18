from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database import Base

class Notification(Base):
    __tablename__ = "notifications"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    message = Column(String, nullable=False)
    type_id = Column(Integer, ForeignKey("notification_types.id"))
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    type = relationship("NotificationType")

