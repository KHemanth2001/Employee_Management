from pydantic import BaseModel, EmailStr, Field, ConfigDict
from typing import Optional
from datetime import date


class CreateEmployeeRequest(BaseModel):
    name: str
    email: EmailStr
    department: Optional[str] = Field(default=None)
    role: Optional[str] = Field(default=None)


class CreateEmployeeResponse(BaseModel):
    message: str = Field(default="Employee created Successfully")


class EmployeeResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    department: Optional[str]
    role: Optional[str]
    date_joined: date

    model_config = ConfigDict(from_attributes=True)


class EmployeeListResponse(BaseModel):
    total: int
    items: list[EmployeeResponse]

    model_config = ConfigDict(from_attributes=True)
