from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from typing import Annotated

from .jwt import jwt_to_data


HTTPScheme = HTTPBearer()


async def get_current_user(token: Annotated[HTTPAuthorizationCredentials, Depends(HTTPScheme)]):
    try:
        user = jwt_to_data(token.credentials)
        if not user:
            HTTPException(status_code=401, detail="Authenticaiton Failed" )
        return user

    except Exception as error:
        print(error)
        raise HTTPException(status_code=401, detail="Authentication Failed")

