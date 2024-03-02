from sqlalchemy import (Boolean, Column, Date, String, text, JSON, Integer, func, TIMESTAMP, ForeignKey)
from sqlalchemy.orm import relationship

from app.models.base import Base


class Manga(Base):
    __tablename__ = 'manga'

    id = Column(String(255), primary_key=True)
    name_manga = Column(String(255), nullable=False)
    author = Column(String(255), nullable=False)
    upload_by = Column(String(255), nullable=False)
    update_at = Column(TIMESTAMP)

    chapter_id = Column(String(255), ForeignKey("chapter.id", ondelete="CASCADE"), nullable=False)
    gener_data_id = Column(String(255), ForeignKey("gener.id", ondelete="CASCADE"), nullable=False)

    chapter = relationship("Chapter", back_populates="chapter", passive_deletes=True)
    gener_data = relationship("GenerData", back_populates="gener_data", passive_deletes=True)
