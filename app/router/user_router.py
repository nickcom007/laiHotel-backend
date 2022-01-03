'''
Contains all RESTful APIs for Customer and associated Cart operation
'''
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..model import schemas
from ..dependencies import get_db
from ..services import user



router = APIRouter(
    prefix="/user"
)


@router.post("/register/guest")
def create_user_guest(user_create: schemas.UserCreate, db: Session = Depends(get_db)):
    '''
    Create user in db
    '''
    user_role = 'ROLE_GUEST'
    db_user = user.get_user(db, username = user_create.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    user_creation = user.create_user(db=db, user=user_create, user_role=user_role)
    
    return user_creation

@router.post("/register/host")
def create_user_host(user_create: schemas.UserCreate, db: Session = Depends(get_db)):
    '''
    Create host user in db
    '''
    user_role = 'ROLE_HOST'
    db_user = user.get_user(db, username = user_create.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    user_creation = user.create_user(db=db, user=user_create, user_role=user_role)
    
    return user_creation
