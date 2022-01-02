'''
Denpendencies injection for apis
'''
from .model.database import SessionLocal

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
