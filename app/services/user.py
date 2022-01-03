'''
All crud operations for user entity
'''
from sqlalchemy.orm import Session
from ..model import schemas
from ..model import models
from ..auth.password import get_password_hash


def get_user(db: Session, username: str):

    return db.query(models.User).filter(models.User.username == username).first()

def create_user(db: Session, user: schemas.UserCreate, user_role: str):

    hashed_password = get_password_hash(user.password)
    db_user = models.User(
        username = user.username, nickname = user.nickname,
        hashed_password = hashed_password
        )
    
    db_role = models.Authority(
        username = user.username,
        authority = user_role
    )
    
    db.add(db_user)
    db.add(db_role)
    db.commit()
    db.refresh(db_user)

    return db_user

def get_user_auth(db: Session, username: str):

    return db.query(models.Authority).filter(models.Authority.username == username).first()