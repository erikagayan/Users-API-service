from fastapi import APIRouter
from database.engine import collection_name
from bson import ObjectId

router = APIRouter()

"""DELETE Request Method"""


@router.delete("/{id}")
async def delete_users(id: str):
    await collection_name.find_one_and_delete({"_id": ObjectId(id)})
