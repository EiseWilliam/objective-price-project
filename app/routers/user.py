from fastapi import APIRouter, Depends, HTTPException, status
from bson.objectid import ObjectId


from db.db import user_response
from utils.utils import get_current_user

from models.schemas import UserUpdateSchema, UserBaseSchema

from db.database import User


router = APIRouter()


@router.get('/', response_model=list)
async def get_me(user : UserBaseSchema = Depends(get_current_user)):
    users = await User.retrieve_users()
    return users

# update account
@router.put('/update', status_code=status.HTTP_200_OK)
async def update_account(user_details: UserUpdateSchema, user_id: str = Depends(get_current_user)) -> dict:
    # check if user exists
    user = User.find_one({'_id': ObjectId(user_id)})
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User not found')
    
    # update user
    user = user_details.dict(exclude_unset=True)
    
    

# delete account
@router.delete('/delete', status_code=status.HTTP_200_OK)
async def delete_account(user_id: str = Depends(get_current_user)) -> dict:
    """_summary_

    Args:
        user_id (str, optional): _description_. Defaults to Depends(oauth2.get_current_user).

    Raises:
        HTTPException: _description_

    Returns:
        dict: _description_
    """
    # check if user exists
    user = User.find_one({'_id': ObjectId(user_id)})
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User not found')
    
    # delete user
    User.delete_one({'_id': ObjectId(user_id)})
    return {'status': 'success', 'message': 'User deleted'}