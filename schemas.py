from pydantic import BaseModel, EmailStr
from typing import Optional
from decimal import Decimal
from pydantic import conint
from enum import Enum


class UserRole(str, Enum):
    SYSTEM_ADMIN = "system-admin"
    AUTHOR = "author"
    CUSTOMER = "customer"


class UserBase(BaseModel):
    username: str
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    phone: Optional[str] = None
    email: EmailStr
    role: UserRole = UserRole.CUSTOMER


class UserCreate(UserBase):
    password: str


class UserResponse(BaseModel):
    id: int
    username: str
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    phone: Optional[str] = None
    email: EmailStr
    role: UserRole

    class Config:
        orm_mode = True


class BookBase(BaseModel):
    title: str
    isbn: str
    price: Decimal
    genre_id: Optional[int] = None
    description: Optional[str] = None
    units: Optional[int] = 1
    author_id: int


class CustomerBase(BaseModel):
    user_id: int
    subscription: str
    subscription_end_time: Optional[conint] = None
    wallet_money: Optional[Decimal] = None


class ReservationBase(BaseModel):
    customer_id: int
    book_id: int
    start_time: conint
    end_time: conint
    price: Decimal


class BookResponse(BookBase):
    id: int

    class Config:
        from_attributes = True


class CustomerResponse(CustomerBase):
    id: int

    class Config:
        from_attributes = True


class ReservationResponse(ReservationBase):
    id: int

    class Config:
        from_attributes = True
