import jwt
import os
from datetime import datetime, timedelta, timezone
from dotenv import load_dotenv, find_dotenv

from ..schemas.schemas import UserOut
from ..schemas.schemas import TokenType

load_dotenv(find_dotenv())
SECRET = os.getenv("JWT_SECRET")
ALGORITHM=os.getenv("JWT_ALGORITHM")
ACCESS_EXPIRY = int(os.getenv("JWT_ACCESS_TOKEN_EXPIRY_HRS"))
REFRESH_EXPIRY = int(os.getenv("JWT_ACCESS_TOKEN_EXPIRY_HRS"))


def data_to_jwt(user: UserOut, type: TokenType):
    to_encode = user.model_dump()
    if type == TokenType.access:
        expire = datetime.now(timezone.utc) + timedelta(hours=ACCESS_EXPIRY)
    else:
        expire = datetime.now(timezone.utc) + timedelta(days=REFRESH_EXPIRY)

    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET, algorithm=ALGORITHM )
    return encoded_jwt


def jwt_to_data(token: str):
    data = jwt.decode(token, SECRET, algorithms=ALGORITHM)
    return data
