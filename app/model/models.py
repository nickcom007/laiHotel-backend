'''
ORM Data model
'''
from os import name
from sqlalchemy import Boolean, Column, ForeignKey, String, BigInteger, SmallInteger, Text, Date
from sqlalchemy.orm import relationship
from .database import Base


class User(Base):
    '''
    User table defination
    '''
    __tablename__ = "user"

    username = Column(String(32), primary_key=True, index=True)
    nickname = Column(String(32))
    hashed_password = Column(String(128))
    enabled = Column(Boolean, default=True)

    authority = relationship("Authority", back_populates="user", uselist=False)

class Authority(Base):
    '''
    Authority table defination
    '''
    __tablename__ = "authority"

    username = Column(String(32), ForeignKey("user.username"), primary_key=True)
    authority = Column(String(32))

    user = relationship("User", back_populates="authority")

class Stay(Base):
    '''
    Stay table defination
    '''
    __tablename__ = "stay"

    id = Column(String(255), index = True, primary_key=True)
    name = Column(String(255))
    address = Column(String(255))
    guest_number = Column(SmallInteger)
    description = Column(Text)
    user_id = Column(String(32), ForeignKey("user.username"))

class StayAvailability(Base):
    '''
    Availability date for all Stay
    '''
    __tablename__ = 'stay_availability'

    date = Column(Date, primary_key=True)
    state = Column(SmallInteger)
    stay_id = Column(String(255), ForeignKey("stay.id"), primary_key=True) 