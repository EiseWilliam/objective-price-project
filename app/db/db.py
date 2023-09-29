from bson.objectid import ObjectId
from db.database import User, db

collection1 = User


# Database serializers
async def user_entity(user) -> dict:
    return {
        "id": str(user["id"]),
        "username": user["username"],
        "email": user["email"],
        "password": user["hashed_password"],
        "verified": user["verified"],
        "created_at": user["created_at"],
        "updated_at": user["updated_at"],
    }


async def user_response(user: User) -> dict:
    await user
    return {
        "id": user["id"],
        "username": user["username"],
        "email": user["email"],
        "created_at": user["created_at"],
        "updated_at": user["updated_at"],
    }


async def userListEntity(users) -> list:
    users = []
    async for user in collection1.find():
        users.append(user_entity(user))
    return users


# retreive all list of users
async def retrieve_users():
    users = []
    async for user in collection1.find():
        users.append(user_response(user))
    return users


# add a created timestamp
async def add_user(user_data: dict) -> dict:
    user = await collection1.insert_one(user_data)
    new_user = await collection1.find_one({"_id": user.inserted_id})
    return user_response(new_user)


# retreive user
async def retrieve_user(user_id: str) -> dict:
    user = await collection1.find_one({"_id": ObjectId(user_id)})
    if user:
        return user_response(user)


# find user by email
async def find_user(email: str) -> dict:
    user = await db.users.find_one({"email": email})
    if user:
        return user_response(user)


# delete user from db
async def delete_user(user_id: str):
    user = await collection1.find_one({"_id": ObjectId(user_id)})
    if user:
        await collection1.delete_one({"_id": ObjectId(user_id)})
        return True
