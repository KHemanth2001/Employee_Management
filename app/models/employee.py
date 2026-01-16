from sqlalchemy import Column, Integer, String, Date
from datetime import date
from app.db.database import Base

class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True, index=True)
    department = Column(String, nullable=True)
    role = Column(String, nullable=True)
    date_joined = Column(Date, default=date.today)
