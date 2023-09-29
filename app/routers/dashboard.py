from fastapi import APIRouter, Depends, HTTPException, status
from bson.objectid import ObjectId


from db.db import user_response, userListEntity, retrieve_users
from utils.utils import get_current_user

from models.schemas import UserUpdateSchema, UserBaseSchema

from db.database import User


router = APIRouter()


# get all users in db
@router.get('/', response_model=list)
async def list_users():
    users = await retrieve_users()
    if users:
        return (users, "Users data retrieved successfully")
    return (users, "Empty list returned")