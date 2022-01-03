from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from datetime import timedelta
from sqlalchemy.orm import Session
from .model import models
from .model.database import engine
from .dependencies import get_db
from .router import user_router, stay_router
from .model import schemas
from .auth.authentication import authenticate_user, create_access_token, get_current_active_user

models.Base.metadata.create_all(bind=engine)
app = FastAPI()
app.include_router(user_router.router)
app.include_router(stay_router.router)

@app.get("/")
def hello():
    return "Welcome to the LaiHotel ^ ^!"


@app.post("/token", response_model= schemas.Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = authenticate_user(
        db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=15)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/user/me")
def get_myself(current_user: schemas.User = Depends(get_current_active_user)):

    return current_user.nickname