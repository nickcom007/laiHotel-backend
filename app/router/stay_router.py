from fastapi import APIRouter, Depends, HTTPException,status
from sqlalchemy.orm import Session
from ..model import schemas
from ..dependencies import get_db
from ..services import stay_service, user
from ..auth.authentication import get_current_active_user



router = APIRouter(
    prefix="/stay"
)

@router.post("/add")
def add_new_stay(stay: schemas.StayCreate, 
                db: Session = Depends(get_db),
                current_user: schemas.User = Depends(get_current_active_user)):
    '''
    Add a new stay by host
    '''
    user_auth = user.get_user_auth(db, username=current_user.username)
    if user_auth.authority != 'ROLE_HOST':
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Your account is not authorized as a host",
            headers={"WWW-Authenticate": "Bearer"},
        )

    stay_creation = stay_service.add_stay(db, stay, current_user)

    return stay_creation