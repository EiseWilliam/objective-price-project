from datetime import datetime
from bson import ObjectId
from pydantic import BaseModel, EmailStr, constr, Extra
from typing import Optional, Any


class UserBaseSchema(BaseModel):
    username: str | None = None
    email: str
    photo: str | None = None
    created_at: datetime | None = None
    updated_at: datetime | None = None

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        json_schema_extra = {
            "example": {
                "id": "60f7c3c5d5e4a3f6d9c7b7c2",
                "name": "John Doe",
                "email": "johndoe@example.com",
                "photo": "https://example.com/johndoe.jpg",
                "created_at": "2023-07-21T12:34:56.789Z",
                "updated_at": "2023-07-21T12:34:56.789Z"
            }
        }




class LoginUserSchema(BaseModel):
    email: EmailStr
    password: str
    


class CreateUserSchema(LoginUserSchema):
    passwordConfirm: str
    
class UserUpdateSchema(BaseModel):
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    photo: Optional[str] = None

    class Config:
        json_schema_extra = {
            "example": {
                "username": "John Doe",
                "email": "example@email.com",
                "photo": "https://example.com/johndoe.jpg"}}
                

  

class UserResponseSchema(UserBaseSchema):
    id: str
    pass


class UserResponse(BaseModel):
    status: str
    user: UserResponseSchema
    
class Token(BaseModel):
    access_token: str
    token_type: str
    
class TokenData(BaseModel):
    username: str 
    email: str


