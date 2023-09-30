from datetime import datetime, timedelta
from typing import Annotated
from bson.objectid import ObjectId
from fastapi import APIRouter, Response, status, Depends, HTTPException, Body

from auth import oauth2
from db.database import User
from db.db import user_entity, user_response, userListEntity
from models.schemas import UserResponse, CreateUserSchema, LoginUserSchema
from utils.utils import hash_password, verify_password, create_access_token, create_refresh_token, get_current_user
from auth import oauth2
from config import settings


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