from fastapi import APIRouter, HTTPException
from database.models import Users
from database.engine import collection_name
from schemas import list_serial, individual_serial
from bson import ObjectId

router = APIRouter()


"""PUT Request Method"""


@router.put("/{id}")
async def put_users(id: str, users: Users):
    await collection_name.find_one_and_update(
        {"_id": ObjectId(id)}, {"$set": dict(users)}
    )
