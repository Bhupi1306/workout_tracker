from fastapi import HTTPException, APIRouter, Depends, Response
from sqlalchemy import or_
from sqlalchemy.orm import Session

from ..db.connect import get_db
from ..db.models import User
from ..schemas.schemas import UserCreate, UserOut
from ..utils.hashing import hash_password
from ..utils.jwt import data_to_jwt

router = APIRouter(tags=["register"])



@router.post('/register', response_model=UserOut)
async def register(user: UserCreate,  response:Response, db: Session = Depends(get_db)):

    if not user.user_name or not user.password or not user.email:
        raise HTTPException(status_code=400, detail="All fields are required")
        
    db_user = db.query(User).filter(or_(User.user_name == user.user_name , User.email == user.email)).first()
    if db_user:
        if db_user.user_name == user.user_name:
            raise HTTPException(status_code=400, detail="Username already exists")
        elif db_user.email == user.email:
            raise HTTPException(status_code=400, detail="Email already exists")
        
    try:
        hashed_password = hash_password(user.password)
    
        stored_user = User(
            user_name=user.user_name,
            email=user.email,
            password=hashed_password
        )

        db.add(stored_user)
        db.commit()
        db.refresh(stored_user)

        user_dict = UserOut.model_validate(stored_user)
        access_token = data_to_jwt(user_dict, 'access')
        refresh_token = data_to_jwt(user_dict, 'refresh')

        response.set_cookie(key="refresh_token", value=refresh_token, httponly=True, secure=False) # Make secure=True in production
        user_dict.token = access_token
        return user_dict

    except Exception as error:
        raise HTTPException(status_code=500, detail=error)
        