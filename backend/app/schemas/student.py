"""Sch?mas Pydantic pour les ?l?ves."""

from datetime import date, datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict


class StudentBase(BaseModel):
    user_id: Optional[int] = None
    matricule: str
    first_name: str
    last_name: str
    date_of_birth: date
    place_of_birth: str
    gender: str
    phone_number: Optional[str] = None
    address: Optional[str] = None
    photo_url: Optional[str] = None
    status: str
    email: Optional[str] = None
    is_active: bool = True


class StudentCreate(StudentBase):
    pass


class StudentUpdate(BaseModel):
    user_id: Optional[int] = None
    matricule: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    date_of_birth: Optional[date] = None
    place_of_birth: Optional[str] = None
    gender: Optional[str] = None
    phone_number: Optional[str] = None
    address: Optional[str] = None
    photo_url: Optional[str] = None
    status: Optional[str] = None
    email: Optional[str] = None
    is_active: Optional[bool] = None


class StudentRead(StudentBase):
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
