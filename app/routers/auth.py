from datetime import datetime, timedelta
from typing import Annotated
from bson.objectid import ObjectId
from fastapi import APIRouter, Response, status, Depends, HTTPException, Body

# from app.auth import oauth2
from db.database import User
from db.db import user_entity, user_response, userListEntity, find_user
from models.schemas import UserResponse, CreateUserSchema, LoginUserSchema
from utils.utils import hash_password, verify_password, create_access_token, create_refresh_token, get_current_user
# from app.auth import oauth2
from config import settings



router = APIRouter()
ACCESS_TOKEN_EXPIRES_IN = settings.ACCESS_TOKEN_EXPIRES_IN
REFRESH_TOKEN_EXPIRES_IN = settings.REFRESH_TOKEN_EXPIRES_IN


@router.post('/register', status_code=status.HTTP_201_CREATED)
async def register(payload: Annotated[CreateUserSchema, Body()], response: Response) -> dict:
    """
    Register a new user.

    Args:
        payload: A CreateUserSchema object containing the user's email, password, and password confirmation.

    Returns:
        A dictionary containing the status of the operation and the newly created user object.
    """
    # Check if user already exists
    user = find_user(payload.email.lower())
    if user:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail='User already registered')

    # Compare and confirm password
    if payload.password != payload.passwordConfirm:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Password does not match')

    # Hash the password
    payload.password = hash_password(payload.password)
    new_user = {"new_user": payload.model_dump()}
    new_user["email"] = payload.email.lower()
    new_user["created_at"] = datetime.utcnow()
    new_user["updated_at"] = new_user["created_at"]

    # Insert the new user into the database
    User.insert_one(new_user)
    feedback_user = await user_response(User.find_one({'email': new_user["email"]}))
    feedback_user = user_response(feedback_user)
    
    # login user
    access_token = create_access_token(
        subject=str(feedback_user["id"]), expires_time=timedelta(minutes=ACCESS_TOKEN_EXPIRES_IN))
    
        # Create refresh token
    refresh_token = create_refresh_token(
        subject=str(user["id"]), expires_time=timedelta(minutes=REFRESH_TOKEN_EXPIRES_IN))

    # Store refresh and access tokens in cookie
    response.set_cookie('access_token', access_token, ACCESS_TOKEN_EXPIRES_IN * 60,
                        ACCESS_TOKEN_EXPIRES_IN * 60, '/', None, False, True, 'lax')
    response.set_cookie('refresh_token', refresh_token,
                        REFRESH_TOKEN_EXPIRES_IN * 60, REFRESH_TOKEN_EXPIRES_IN * 60, '/', None, False, True, 'lax')
    response.set_cookie('logged_in', 'True', ACCESS_TOKEN_EXPIRES_IN * 60,
                        ACCESS_TOKEN_EXPIRES_IN * 60, '/', None, False, False, 'lax')

    # Send both access
    return {'status': 'success', 'access_token': access_token}

# User sign in
@router.post('/login', status_code=status.HTTP_200_OK, response_model=UserResponse)
async def login(payload: LoginUserSchema, response: Response) -> dict:
    """_summary_

    Args:
        payload (LoginUserSchema): _description_
        response (Response): _description_

    Raises:
        HTTPException: _description_
        HTTPException: _description_

    Returns:
        dict: _token_
    """
    
    # check if user exists
    user = User.find_one({'email': payload.email.lower()})
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User not found')
    user = user_entity(user)
    
    # check if password is correct
    if not await verify_password(payload.password, user['hashed_password']):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Incorrect password')
    
    # create access token
    access_token = create_access_token(
        subject=str(user["id"]), expires_time=timedelta(minutes=ACCESS_TOKEN_EXPIRES_IN))

    # Create refresh token
    refresh_token = create_refresh_token(
        subject=str(user["id"]), expires_time=timedelta(minutes=REFRESH_TOKEN_EXPIRES_IN))

    # Store refresh and access tokens in cookie
    response.set_cookie('access_token', access_token, ACCESS_TOKEN_EXPIRES_IN * 60,
                        ACCESS_TOKEN_EXPIRES_IN * 60, '/', None, False, True, 'lax')
    response.set_cookie('refresh_token', refresh_token,
                        REFRESH_TOKEN_EXPIRES_IN * 60, REFRESH_TOKEN_EXPIRES_IN * 60, '/', None, False, True, 'lax')
    response.set_cookie('logged_in', 'True', ACCESS_TOKEN_EXPIRES_IN * 60,
                        ACCESS_TOKEN_EXPIRES_IN * 60, '/', None, False, False, 'lax')

    # Send both access
    return {'status': 'success', 'access_token': access_token}

# user logout
@router.post('/logout', status_code=status.HTTP_200_OK)
async def logout(response: Response) -> dict:
    """_summary_

    Args:
        response (Response): _description_

    Returns:
        dict: _description_
    """
    # Clear cookies
    response.delete_cookie('access_token')
    response.delete_cookie('refresh_token')
    response.delete_cookie('logged_in')

    return {'status': 'success', 'message': 'User logged out'}



   


# sign up with google
# @router.post('/google', status_code=status.HTTP_201_CREATED, response_model=UserResponse)
# async def google_signup(token: str) -> dict:
#     """
#     Sign up a new user using Google OAuth2 authentication.

#     Args:
#         token: A string containing the user's Google ID token.

#     Returns:
#         A dictionary containing the status of the operation and the newly created user object.
#     """
#     try:
#         # Verify the authenticity of the Google ID token
#         idinfo = id_token.verify_oauth2_token(token, requests.Request())

#         # Extract the user's email and name from the token
#         email = idinfo['email']
#         name = idinfo['name']

#         # Check if user already exists in the database
#         user = User.find_one({'email': email})
#         if user:
#             # User already exists, return user information
#             return {"status": "success", "user": user}

#         # User does not exist, create a new user object and insert it into the database
#         new_user = User(email=email, name=name, created_at=datetime.utcnow(), updated_at=datetime.utcnow())
#         result = new_user.insert_one()

#         # Retrieve the newly created user object from the database and return it
#         new_user = User.find_one({'_id': result.inserted_id})
#         return {"status": "success", "user": new_user}

#     except ValueError:
#         # Invalid token
#         raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Invalid token')



    
    
