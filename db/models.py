import uuid

from sqlalchemy import UUID, Boolean, Column, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(255), nullable=False)
    surname = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False, unique=True)
    about_me = Column(String(255), nullable=False)
    as_active = Column(Boolean, default=True)
