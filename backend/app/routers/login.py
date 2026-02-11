from fastapi import APIRouter, Depends, HTTPException, Response
from sqlalchemy.orm import Session

from ..db.connect import get_db
from ..db.models import User
from ..schemas.schemas import UserOut, UserLogin
from ..utils.hashing import hash_password, verify_password
from ..utils.jwt import data_to_jwt

router = APIRouter(tags=["login"])

@router.post('/login', response_model=UserOut)
def login(user: UserLogin,response: Response, db: Session = Depends(get_db)):

    try:
        if not user.email or not user.password:
            raise HTTPException(status_code=400, detail="All fields are required")

        db_user = db.query(User).filter(User.email == user.email).first()

        if not db_user:
            raise HTTPException(status_code=400, detail="User with this email does not exists")
        
        verify = verify_password(user.password, str(db_user.password))
        if not verify:
            raise HTTPException(status_code=400, detail="invalid password")
            
        user_dict = UserOut.model_validate(db_user)
        access_token = data_to_jwt(user_dict, 'access')
        refresh_token = data_to_jwt(user_dict, 'refresh')

        response.set_cookie(key="refresh_token", value=refresh_token, httponly=True, secure=False) # Make secure=True in production
        user_dict.token = access_token
        

        return user_dict

        
    
    except Exception as error:
        raise HTTPException(status_code=500, detail="Something went wrong")
