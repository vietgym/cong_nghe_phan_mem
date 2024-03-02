from sqlalchemy import (Column, String, ForeignKey)
from sqlalchemy.orm import relationship

from app.models.base import Base


class Image(Base):
    __tablename__ = 'image'

    id = Column(String(255), primary_key=True)
    image = Column(String(255), nullable=False)
    number_chapter = Column(String(255), nullable=False)
    title = Column(String(255), nullable=False)

