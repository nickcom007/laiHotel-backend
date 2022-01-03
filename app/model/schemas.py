'''
Pydantic Schema for request validation
'''
from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None


class UserBase(BaseModel):

    username: str
    nickname: Optional[str]

class UserCreate(UserBase):

    password: str

class User(UserBase):

    enbled: bool

    class Config:
        orm_mode = True

'''
Authority Schema
'''

class Authority(BaseModel):

    username: str
    role: str

    class Config:
        orm_model = True


class Reservation(BaseModel):

    id: int
    checkin_date: datetime
    checkout_date: datetime
    user_id: str
    stay_id: int
    
    class Config:
        orm_model = True


class StayCreate(BaseModel):
    
    name: str
    address: str
    guest_number: int
    description: str

class Stay(StayCreate):

    class Config:
        orm_model = True

class StayAvailability(BaseModel):

    date: datetime
    state: int
    stay_id: int
    
    class Config:
        orm_model = True
    
class StayImage(BaseModel):

    stay_id: int
    url: str
    
    class Config:
        orm_model = True
