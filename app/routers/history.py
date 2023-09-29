from datetime import datetime, timedelta
from typing import Annotated
from bson.objectid import ObjectId
from fastapi import APIRouter, Response, status, Depends, HTTPException, Body

from app.auth import oauth2
from app.db.database import User
from app.db.db import user_entity, user_response, userListEntity
from app.models.schemas import UserResponse, CreateUserSchema, LoginUserSchema
from app.utils.utils import hash_password, verify_password, create_access_token, create_refresh_token, get_current_user
from app.auth import oauth2
from app.config import settings


router = APIRouter()


@router.get('/', status_code=status.HTTP_200_OK)
async def get_all_activity( user : Annotated [str, Depends(get_current_user)]):

    return {"status": "success", "message": "history page"}

@router.get('/{id}', status_code=status.HTTP_200_OK)
async def get_activity(id: str,  user : Annotated [str, Depends(get_current_user)]):

    return {"status": "success", "message": "history page"}

@router.delete('/{id}', status_code=status.HTTP_200_OK)
async def delete_activity(id: str,  user : Annotated [str, Depends(get_current_user)]):
    return {"status": "success", "message": "history page"}