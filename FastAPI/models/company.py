from backend.db import Base
from sqlalchemy import Column, Integer, String


class Company(Base):
    """Класс определения колонок формы опросного листа"""
    __tablename__ = 'Vysota_company'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True, index=True)
    company = Column(String, nullable=False)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    address = Column(String, nullable=False)
    description = Column(String, nullable=False)
