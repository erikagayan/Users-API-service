from fastapi import APIRouter, HTTPException
from database.engine import collection_name
from schemas import individual_serial
from bson import ObjectId

router = APIRouter()


"""GET Request Method by id"""


@router.get("/{id}")
async def get_user_by_id(id: str):
    user = await collection_name.find_one({"_id": ObjectId(id)})
    if user:
        return individual_serial(user)
    else:
        raise HTTPException(status_code=404, detail="User not found")
