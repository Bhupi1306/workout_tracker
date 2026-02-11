from fastapi import APIRouter,Cookie,HTTPException

from ..schemas.schemas import UserOut
from ..utils.jwt import jwt_to_data, data_to_jwt

router = APIRouter()

@router.post('/refresh')
def refresh(refresh_token : str = Cookie(None)):

    if not refresh_token:
        raise HTTPException(status_code=401, detail="Missing refresh Token")
    
    try:
        payload_dict = jwt_to_data(refresh_token)
        payload = UserOut(**payload_dict)
        if not payload.id:
            raise HTTPException(status_code=401, detail="Invalid Token")

        new_access_token = data_to_jwt(payload, 'access')
        
        return {
            "access_token": new_access_token,
            "token_type": "bearer"
        }
    
    except Exception as error:
        raise HTTPException(status_code=401, detail="Something went wrong")
