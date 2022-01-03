from os import name
from sqlalchemy.orm import Session
from ..model import schemas
from ..model import models
import uuid
from datetime import date as d
from datetime import timedelta

def add_stay(db: Session, stay: schemas.StayCreate, current_user: schemas.User):
    '''
    This function will create a new stay and automatically
    generates next 30 days availablity
    '''
    stay_id = uuid.uuid4()
    db_stay = models.Stay(
        id = stay_id,
        name = stay.name,
        address = stay.address,
        guest_number = stay.guest_number,
        description = stay.description,
        user_id = current_user.username
    )

    db.add(db_stay)
    # Create 30 days at least
    current = d.today()
    for _ in range(30):
        db_stay_avail = models.StayAvailability(
            date = current,
            state = 1,
            stay_id = stay_id
        )
        db.add(db_stay_avail)
        current = current + timedelta(days=1)
    
    db.commit()
    
    return db_stay
    