from fastapi import APIRouter
from database.models import Users
from database.engine import collection_name
from schemas import list_serial
from bson import ObjectId

router = APIRouter()

"""GET Request Method"""
@router.get("/")
async def get_users():
    users = await list_serial(collection_name.find())
    return users


"""POST Request Method"""
@router.post("/")
async def post_users(users: Users):
    await collection_name.insert_one(users.dict())


"""PUT Request Method"""
@router.put("/{id}")
async def put_users(id: str, users: Users):
    await collection_name.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(users)})


"""DELETE Request Method"""
@router.delete("/{id}")
async def delete_users(id: str):
    await collection_name.find_one_and_delete({"_id": ObjectId(id)})
