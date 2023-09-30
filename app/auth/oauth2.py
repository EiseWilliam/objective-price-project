import base64
from typing import List
from jose import JWTError, jwt
from pydantic import BaseModel
from fastapi import Depends, HTTPException, status
from bson.objectid import ObjectId

from db.db import user_entity
from db.database import User

from config import settings



class NotVerified(Exception):
    pass


class UserNotFound(Exception):
    pass


def get_current_user(Authorize: jwt = Depends()):
    try:
        Authorize.jwt_required()
        user_id = Authorize.get_jwt_subject()
        user = user_entity(User.find_one({'_id': ObjectId(str(user_id))}))

        if not user:
            raise UserNotFound('User no longer exist')

        if not user["verified"]:
            raise NotVerified('You are not verified')

    except Exception as e:
        error = e.__class__.__name__
        print(error)
        if error == 'MissingTokenError':
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail='You are not logged in')
        if error == 'UserNotFound':
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail='User no longer exist')
        if error == 'NotVerified':
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail='Please verify your account')
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail='Token is invalid or has expired')
    return user_id
