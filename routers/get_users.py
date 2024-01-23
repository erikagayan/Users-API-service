from fastapi import APIRouter
from database.engine import collection_name
from schemas import list_serial

router = APIRouter()

"""GET Request Method"""


@router.get("/")
async def get_users():
    users = await list_serial(collection_name.find())
    return users
