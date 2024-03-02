from sqlalchemy import (Column, String, ForeignKey)
from sqlalchemy.orm import relationship

from app.models.base import Base


class Chapter(Base):
    __tablename__ = 'chapter'

    id = Column(String(255), primary_key=True)
    manga_name = Column(String(255), nullable=False)
    number_chapter = Column(String(255), nullable=False)
    title = Column(String(255), nullable=False)

    image_data_id = Column(String(255), ForeignKey("image_data.id", ondelete="CASCADE"), nullable=False)
    manga_id = Column(String(255), ForeignKey("manga", ondelete="CASCADE"), nullable=False)

    image_data = relationship("ImageData", back_populates="image_data", passive_deletes=True)
    manga = relationship("Manga", back_populates="manga", passive_deletes=True)
