from sqlalchemy import (Boolean, Column, Date, String, text, JSON, Integer, func, TIMESTAMP, ForeignKey)
from sqlalchemy.orm import relationship

from app.models.base import Base


class GenerData(Base):
    __tablename__ = 'gener_data'

    id = Column(String(255), primary_key=True)
    manga_name = Column(String(255), nullable=False)

    gener_id = Column(String(255), ForeignKey("gener.id", ondelete="CASCADE"), nullable=False)

    gener = relationship("Gener", back_populates="gener", passive_deletes=True)
