from sqlalchemy import (Boolean, Column, Date, String, text, JSON, Integer, func, TIMESTAMP, ForeignKey)
from sqlalchemy.orm import relationship

from app.models.base import Base


class Gener(Base):
    __tablename__ = 'gener'

    id = Column(String(255), primary_key=True)
    gener_value = Column(String(255), nullable=False)
