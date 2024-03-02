from sqlalchemy import (Column, String, ForeignKey)
from sqlalchemy.orm import relationship

from .base import Base, UserSystemRole, UserMangaRole


class User(Base):
    __tablename__ = "user"

    id = Column(String(255), primary_key=True)
    username = Column(String(42), nullable=False, index=True)
    email = Column(String(255), nullable=False, index=True)
    password = Column(String(255))
    full_name = Column(String(255))
    role_system = Column(String(), default=UserSystemRole.MEMBER)
    role_manga = Column(String(), default=UserMangaRole.VIEWER)

    manga_id = Column(String(255), ForeignKey("user.id", ondelete="CASCADE"), nullable=True)

    manga = relationship("Manga", back_populates="manga", passive_deletes=True)
