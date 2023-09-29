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

# free access features
@router.get('/search/{item}', status_code=status.HTTP_200_OK)
async def search(item: str, user : Annotated [str, Depends(get_current_user) ] ):
    
    
    # on success log to user  history
    
    
    
    return {"status": "success", "message": "search page"}

# Authenticated features
