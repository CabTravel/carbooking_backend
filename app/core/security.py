
from datetime import datetime,timedelta,timezone

from uuid import UUID
from jose import jwt
from fastapi import Header,HTTPException,status

SECRET_KEY='MY_NAME_IS_DINESH'
ALGORITHM='HS256'
ACCESS_TOKEN_EXPIRE_MINUTES=60*24*365

def create_access_token(user_id:UUID)->str:
    expire=datetime.now(timezone.utc)+timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    payload={
        'userId':str(user_id),
        'exp':expire    
    }
    return jwt.encode(payload,SECRET_KEY,algorithm=ALGORITHM)



def get_current_user_id(authToken:str|None=Header(default=None,alias='authToken'))->UUID:

    if authToken is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
         detail='Authentication token is required'
                            )

    try:
        payload=jwt.decode(authToken,SECRET_KEY,algorithms=[ALGORITHM])

        userId=payload.get('userId')

        if userId is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail='Invalid authentication token'
            )
        return UUID(userId)

    except :
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Invalid or expired authentication token'
        )

    
    


