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

# free access features
@router.get('/search/{item}', status_code=status.HTTP_200_OK)
async def search(item: str, user : Annotated [str, Depends(get_current_user) ] ):
    
    
    # on success log to user  history
    
    
    
    return {"status": "success", "message": "search page"}

# Authenticated features
